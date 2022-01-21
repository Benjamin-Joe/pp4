from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    "Form for creating blog posts"
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'content', 'post_image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class SearchForm(forms.Form):
    "Form for searching for posts"
    q = forms.CharField()


class CommentForm(forms.ModelForm):
    "Form for commenting on posts"
    class Meta:
        "Class to select form fields and edit form styling"
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-10'}),
            'email': forms.TextInput(attrs={'class': 'col-10'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        },
