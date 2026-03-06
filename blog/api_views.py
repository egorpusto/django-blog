from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post
from .serializers import PostDetailSerializer, PostListSerializer


class PostListAPIView(generics.ListAPIView):
    """
    Returns a paginated list of all published posts.
    """

    queryset = Post.published.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetailAPIView(generics.RetrieveAPIView):
    """
    Returns a single published post with comments.
    """

    queryset = Post.published.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
