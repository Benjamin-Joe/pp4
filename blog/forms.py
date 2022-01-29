"Forms.py file"
from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    "Form for creating blog posts"
    class Meta:
        "Meta class for PostForm"
        model = Post
        fields = (
            'title', 'slug', 'author', 'category', 'content',
            'post_image', 'status'
            )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'type': 'hidden',
                                             'value': '',
                                             'id': 'user1'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'type': 'hidden'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        },
