from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Comment, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "name", "email", "body", "created", "active")
        read_only_fields = ("created",)


class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="blog-api:post-detail",
        lookup_field="pk",
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "url",
            "title",
            "author",
            "publish",
            "tags",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "author",
            "body",
            "publish",
            "created",
            "updated",
            "status",
            "tags",
            "comments",
        )
