from django.urls import path

from . import views


urlpatterns = [
    path("", views.first_page),
    path("posts/", views.posts),
    path("posts/<slug:slug>", views.post)
]
