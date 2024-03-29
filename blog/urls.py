from django.urls import path

from . import views


urlpatterns = [
    path("", views.first_page.as_view(), name="first-page"),
    path("posts/", views.posts.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.post.as_view(), name="post-detail-page")
]
