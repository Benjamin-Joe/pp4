"Main views.py file"
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm


def homepage(request):
    "View for the homepage"
    posts = Post.postmanager.all()
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, post):
    "View for individual blog posts"
    post = get_object_or_404(Post, slug=post, status='1')
    comments = post.comments.filter(active=True)
    user_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form})


class CategoryView(ListView):
    "Class for creating dropdown list of categories"
    template_name = 'category.html'
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status=1)
        }
        return content
