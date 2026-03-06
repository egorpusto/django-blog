from blog.forms import CommentForm, EmailPostForm


class TestCommentForm:
    def test_valid_data(self):
        form = CommentForm(
            data={
                "name": "Alice",
                "email": "alice@example.com",
                "body": "Nice post!",
            }
        )
        assert form.is_valid()

    def test_missing_name(self):
        form = CommentForm(
            data={
                "name": "",
                "email": "alice@example.com",
                "body": "Nice post!",
            }
        )
        assert not form.is_valid()
        assert "name" in form.errors

    def test_invalid_email(self):
        form = CommentForm(
            data={
                "name": "Alice",
                "email": "not-an-email",
                "body": "Nice post!",
            }
        )
        assert not form.is_valid()
        assert "email" in form.errors


class TestEmailPostForm:
    def test_valid_data(self):
        form = EmailPostForm(
            data={
                "name": "Bob",
                "email": "bob@example.com",
                "to": "friend@example.com",
                "comments": "Check this out!",
            }
        )
        assert form.is_valid()

    def test_comments_not_required(self):
        form = EmailPostForm(
            data={
                "name": "Bob",
                "email": "bob@example.com",
                "to": "friend@example.com",
                "comments": "",
            }
        )
        assert form.is_valid()
