from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')


admin.site.register(models.Post, PostAdmin)


admin.site.register(models.Comment)