"Main project url file"
from django.urls import path
from . import views

app_name = 'BLOG'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search, name='search'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('category/<category>/', views.CategoryView.as_view(), name='category'),
]
