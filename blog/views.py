"Main views.py file"
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from django.db.models import Q
from .forms import CommentForm, SearchForm, PostForm


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


class CreatePost(CreateView):
    "View for creating a post via a post form"
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'


class DeletePost(DeleteView):
    "View for deleting a blog post"
    model = Post
    template_name = 'delete_post.html'
    success_url = ('/')


class EditPost(UpdateView):
    "Class for updating blog posts"
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'category', 'content']


def categorydropdown(request):
    "Function to call all categories"
    categorydropdown = Category.objects.all()
    context = {
        'categorydropdown': categorydropdown,
    }
    return context


def search(request):
    "View for searching for posts"
    form = SearchForm()
    q = ''
    results = []
    query = Q()

    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            if q is not None:
                query &= Q(title__contains=q)
            results = Post.objects.filter(query)
    return render(request, 'search_bar.html', {'form': form, 'q': q, 'results': results})
