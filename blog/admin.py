"Admin.py file"
from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    "Class for displaying posts in admin section"
    list_display = ('title', 'author', 'category', 'created_on')
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    "Class for displaying comments in admin section"
    list_display = ('post', 'name', 'email', 'content', 'active')
    search_fields = ('name', 'email', 'content')


admin.site.register(models.Category)
