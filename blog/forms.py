from django import forms
from .models import Comment


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
