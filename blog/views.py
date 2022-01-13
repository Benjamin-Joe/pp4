"Main views.py file"
from django.shortcuts import render


def homepage(request):
    "View for the homepage"
    return render(request, 'index.html')
