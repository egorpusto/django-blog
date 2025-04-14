from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Views using class-based views
    # path("", views.PostListView.as_view(), name='post_list'),
    path("", views.post_list, name='post_list'),
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
    )
]
