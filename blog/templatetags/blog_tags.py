from django import template
from django.core.cache import cache
from django.db.models import Count
from django.utils.safestring import mark_safe

import markdown

from ..models import Post

register = template.Library()


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_posts():
    count = cache.get("total_posts")
    if count is None:
        count = Post.published.count()
        cache.set("total_posts", count, 60 * 15)
    return count


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    cache_key = f"latest_posts_{count}"
    latest_posts = cache.get(cache_key)
    if latest_posts is None:
        latest_posts = list(Post.published.order_by("-publish")[:count])
        cache.set(cache_key, latest_posts, 60 * 15)
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    cache_key = f"most_commented_{count}"
    posts = cache.get(cache_key)
    if posts is None:
        posts = list(
            Post.published.annotate(total_comments=Count("comments")).order_by(
                "-total_comments"
            )[:count]
        )
        cache.set(cache_key, posts, 60 * 15)
    return posts
