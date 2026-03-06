from django.contrib.auth.models import User
from django.core.cache import cache
from django.urls import reverse
from django.utils import timezone

import pytest

from blog.models import Comment, Post


@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()
    yield
    cache.clear()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser",
        password="testpass123",
    )


@pytest.fixture
def post(user):
    return Post.objects.create(
        title="Test Post",
        slug="test-post",
        author=user,
        body="Test body content.",
        status=Post.Status.PUBLISHED,
        publish=timezone.now(),
    )


class TestPostListView:
    def test_returns_200(self, client, post):
        url = reverse("blog:post_list")
        response = client.get(url)
        assert response.status_code == 200

    def test_shows_published_post(self, client, post):
        url = reverse("blog:post_list")
        response = client.get(url)
        assert "Test Post" in response.content.decode()

    def test_draft_not_shown(self, client, user):
        Post.objects.create(
            title="Hidden Draft",
            slug="hidden-draft",
            author=user,
            body="body",
            status=Post.Status.DRAFT,
            publish=timezone.now(),
        )
        url = reverse("blog:post_list")
        response = client.get(url)
        assert "Hidden Draft" not in response.content.decode()


class TestPostDetailView:
    def test_returns_200(self, client, post):
        url = post.get_absolute_url()
        response = client.get(url)
        assert response.status_code == 200

    def test_draft_returns_404(self, client, user):
        draft = Post.objects.create(
            title="Draft",
            slug="draft",
            author=user,
            body="body",
            status=Post.Status.DRAFT,
            publish=timezone.now(),
        )
        url = draft.get_absolute_url()
        response = client.get(url)
        assert response.status_code == 404


class TestPostCommentView:
    def test_valid_comment_is_saved(self, client, post):
        url = reverse("blog:post_comment", args=[post.id])
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "body": "Great post!",
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert Comment.objects.filter(post=post, name="Alice").exists()

    def test_invalid_comment_not_saved(self, client, post):
        url = reverse("blog:post_comment", args=[post.id])
        data = {"name": "", "email": "bad-email", "body": ""}
        client.post(url, data)
        assert Comment.objects.filter(post=post).count() == 0

    def test_get_not_allowed(self, client, post):
        url = reverse("blog:post_comment", args=[post.id])
        response = client.get(url)
        assert response.status_code == 405


@pytest.mark.django_db
class TestPostShareView:
    def test_get_returns_200(self, client, post):
        url = reverse("blog:post_share", args=[post.id])
        response = client.get(url)
        assert response.status_code == 200

    def test_post_invalid_form(self, client, post):
        url = reverse("blog:post_share", args=[post.id])
        response = client.post(url, {"name": "", "email": "bad", "to": "bad"})
        assert response.status_code == 200
        assert response.context["sent"] is False


@pytest.mark.django_db
class TestPostSearchView:
    def test_empty_form_shown(self, client):
        url = reverse("blog:post_search")
        response = client.get(url)
        assert response.status_code == 200

    def test_search_with_query(self, client, post):
        url = reverse("blog:post_search")
        response = client.get(url, {"query": post.title})
        assert response.status_code == 200
        assert response.context["query"] == post.title
