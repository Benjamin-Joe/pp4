"Main views.py file"
from django.shortcuts import render
from .models import Post


def homepage(request):
    "View for the homepage"
    posts = Post.postmanager.all()

    return render(request, 'index.html', {'posts': posts})
