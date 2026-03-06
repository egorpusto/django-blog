from django.contrib.auth.models import User
from django.utils import timezone

import pytest

from blog.models import Comment, Post


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


@pytest.fixture
def draft_post(user):
    return Post.objects.create(
        title="Draft Post",
        slug="draft-post",
        author=user,
        body="Draft body.",
        status=Post.Status.DRAFT,
        publish=timezone.now(),
    )


class TestPostModel:
    def test_str(self, post):
        assert str(post) == "Test Post"

    def test_get_absolute_url(self, post):
        url = post.get_absolute_url()
        assert str(post.publish.year) in url
        assert post.slug in url

    def test_published_manager_returns_only_published(self, post, draft_post):
        published = Post.published.all()
        assert post in published
        assert draft_post not in published

    def test_default_status_is_draft(self, user):
        post = Post(title="New", slug="new", author=user, body="body")
        assert post.status == Post.Status.DRAFT

    def test_ordering_by_publish_descending(self, user, db):
        post1 = Post.objects.create(
            title="First",
            slug="first",
            author=user,
            body="body",
            status=Post.Status.PUBLISHED,
            publish=timezone.now(),
        )
        post2 = Post.objects.create(
            title="Second",
            slug="second",
            author=user,
            body="body",
            status=Post.Status.PUBLISHED,
            publish=timezone.now(),
        )
        posts = list(Post.published.all())
        assert posts.index(post2) < posts.index(post1)


class TestCommentModel:
    def test_str(self, post):
        comment = Comment.objects.create(
            post=post,
            name="John",
            email="john@example.com",
            body="Nice post!",
        )
        assert "John" in str(comment)
        assert "Test Post" in str(comment)

    def test_comment_active_by_default(self, post):
        comment = Comment.objects.create(
            post=post,
            name="Jane",
            email="jane@example.com",
            body="Great!",
        )
        assert comment.active is True
