"Main project url file"
from django.urls import path
from . import views

app_name = 'BLOG'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search, name='search'),
    path('news/', views.NewsPage, name='NewsPage'),
    path('edit/', views.UserProfile.as_view(), name='edit_profile'),
    path('create/', views.CreatePost.as_view(), name='CreatePost'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('update/<slug>/', views.EditPost.as_view(), name='EditPost'),
    path('delete/<slug>/', views.DeletePost.as_view(), name='DeletePost'),
    path('like/<slug:slug>', views.LikeView, name='like_post'),
    path('category/<category>/', views.CategoryView.as_view(), name='category')
]
