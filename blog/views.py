from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post


def first_page(request):
    # see the first page here
    posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/first_page.html", context={
        "posts": posts
    })


def posts(request):
    # see posts here

    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", context={
        "posts": posts
    })


def post(request, slug):
    # see indivisual post here

    my_post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post.html", context={
        "post": my_post,
        "post_tags": my_post.tags.all()
    })