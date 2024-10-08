from django.urls import path

from . import views


urlpatterns = [
    path("", views.first_page, name="first-page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post, name="post-detail-page")
]
