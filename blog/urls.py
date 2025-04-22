from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name = 'blog'

urlpatterns = [
    # Views using class-based views
    # path("", views.PostListView.as_view(), name='post_list'),
    path("", views.post_list, name='post_list'),
    path(
        'tag/<slug:tag_slug>/',
        views.post_list,
        name='post_list_by_tag'
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
          views.post_detail, 
          name='post_detail'
          ),
    path(
        'share/<int:post_id>/',
        views.post_share,
        name='post_share'
    ),
    path(
        'comment/<int:post_id>/',
        views.post_comment,
        name='post_comment'
    ),
    path(
        'feed/',
        LatestPostsFeed(),
        name='post_feed'
    ),
    path(
        'search/',
        views.post_search,
        name='post_search'
    ),
]
