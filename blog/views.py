from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView


class first_page(ListView):
    template_name = "blog/first_page.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        query_set =  super().get_queryset()
        return query_set.order_by("-date")[:3]
    

class posts(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.order_by("-date")

class post(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all() 
        return context
    