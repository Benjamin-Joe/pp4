"Main views.py file"
from django.shortcuts import render, get_object_or_404
from .models import Post


def homepage(request):
    "View for the homepage"
    posts = Post.postmanager.all()

    return render(request, 'index.html', {'posts': posts})


def post_detail(request, post):
    "View for individual blog posts"
    post = get_object_or_404(Post, slug=post, status='1')
    return render(request, 'post_detail.html', {'post': post})
