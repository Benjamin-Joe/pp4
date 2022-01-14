"Main project url file"
from django.urls import path
from . import views

app_name = 'BLOG'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]
