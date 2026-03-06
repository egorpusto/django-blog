import logging

from django.contrib.postgres.search import TrigramSimilarity
from django.core.cache import cache
from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, FormView, ListView

from taggit.models import Tag

from .forms import CommentForm, EmailPostForm, SearchForm
from .models import Post

logger = logging.getLogger(__name__)

CACHE_TTL_LIST = 60 * 5
CACHE_TTL_DETAIL = 60 * 10
CACHE_TTL_SIDEBAR = 60 * 15


class PostListView(ListView):
    """
    Displays a paginated list of published posts.
    Optionally filtered by tag.
    """

    template_name = "blog/post/list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        self.tag = None
        tag_slug = self.kwargs.get("tag_slug")

        cache_key = f"post_list_{tag_slug or 'all'}"
        queryset = cache.get(cache_key)

        if queryset is None:
            queryset = Post.published.all()
            if tag_slug:
                self.tag = get_object_or_404(Tag, slug=tag_slug)
                queryset = queryset.filter(tags__in=[self.tag])
            cache.set(cache_key, queryset, CACHE_TTL_LIST)
        else:
            if tag_slug:
                self.tag = get_object_or_404(Tag, slug=tag_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = getattr(self, "tag", None)
        return context


class PostDetailView(DetailView):
    """
    Displays a single published post with comments and similar posts.
    """

    template_name = "blog/post/detail.html"
    context_object_name = "post"

    def get_object(self):
        cache_key = (
            f"post_detail_"
            f"{self.kwargs['year']}_"
            f"{self.kwargs['month']}_"
            f"{self.kwargs['day']}_"
            f"{self.kwargs['post']}"
        )
        post = cache.get(cache_key)

        if post is None:
            post = get_object_or_404(
                Post,
                status=Post.Status.PUBLISHED,
                publish__year=self.kwargs["year"],
                publish__month=self.kwargs["month"],
                publish__day=self.kwargs["day"],
                slug=self.kwargs["post"],
            )
            cache.set(cache_key, post, CACHE_TTL_DETAIL)

        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        post_tags_ids = post.tags.values_list("id", flat=True)
        similar_posts = (
            Post.published.filter(tags__in=post_tags_ids)
            .exclude(id=post.id)
            .annotate(same_tags=Count("tags"))
            .order_by("-same_tags", "-publish")[:4]
        )

        context["comments"] = post.comments.filter(active=True)
        context["form"] = CommentForm()
        context["similar_posts"] = similar_posts
        return context


class PostShareView(FormView):
    """
    Allows sharing a post via email.
    """

    template_name = "blog/post/share.html"
    form_class = EmailPostForm

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.post_obj = get_object_or_404(
            Post,
            id=self.kwargs["post_id"],
            status=Post.Status.PUBLISHED,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.post_obj
        context["sent"] = False
        return context

    def form_valid(self, form):
        cd = form.cleaned_data
        post_url = self.request.build_absolute_uri(self.post_obj.get_absolute_url())
        subject = f"{cd['name']} recommends you read {self.post_obj.title}"
        message = (
            f"Read {self.post_obj.title} at {post_url}\n\n"
            f"{cd['name']}'s comments: {cd['comments']}"
        )
        send_mail(
            subject,
            message,
            (
                self.request.user.email
                if self.request.user.is_authenticated
                else "noreply@myblog.com"
            ),
            [cd["to"]],
        )
        return render(
            self.request,
            self.template_name,
            {"post": self.post_obj, "form": form, "sent": True},
        )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        cache_key = (
            f"post_detail_"
            f"{post.publish.year}_"
            f"{post.publish.month}_"
            f"{post.publish.day}_"
            f"{post.slug}"
        )
        cache.delete(cache_key)

    return render(
        request,
        "blog/post/comment.html",
        {"post": post, "form": form, "comment": comment},
    )


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = (
                Post.published.annotate(
                    similarity=TrigramSimilarity("title", query),
                )
                .filter(similarity__gt=0.1)
                .order_by("-similarity")
            )

    return render(
        request,
        "blog/post/search.html",
        {"form": form, "query": query, "results": results},
    )
