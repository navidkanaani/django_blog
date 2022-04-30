from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    selected_post = get_object_or_404(Post, slug=slug)
    # selected_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": selected_post,
        "post_tags": selected_post.tag.all(),
    })
