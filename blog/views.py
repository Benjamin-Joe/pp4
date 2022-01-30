"Main views.py file"
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.forms import UserChangeForm
from django.core.paginator import Paginator

from .models import Post, Category
from .forms import CommentForm, SearchForm, PostForm, EditForm


class UserProfile(CreateView):
    "View for user profile"
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = ('/')


def LikeView(request, slug):
    "View for liking blog posts"
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        post.save()
    else:
        post.likes.add(request.user)
        liked = True
        post.save()
    return HttpResponseRedirect('/' + post.slug,)




def NewsPage(request):
    "View for news webpage"
    return render(request, 'news.html')


def homepage(request):
    "View for the homepage"
    posts = Post.postmanager.all()

    pages = Paginator(Post.postmanager.all(), 6)
    page = request.GET.get('page')
    postpage = pages.get_page(page)
    context = {'posts': posts, 'postpage': postpage}
    return render(request, 'index.html', context)


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
    context = {
        'post': post,
        'user_comments': user_comment,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)


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
    form_class = EditForm
    template_name = 'edit_post.html'


def categorydropdown(request):
    "Function to call all categories"
    categorydropdown1 = Category.objects.all()
    context = {
        'categorydropdown1': categorydropdown1,
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
    context = {'form': form, 'q': q, 'results': results}
    return render(request, 'search_bar.html', context)
