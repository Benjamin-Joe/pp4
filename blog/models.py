"Models page for blog"
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
# Post model directly from Django Central

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(models.Model):
    "Class for blog categories"
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        "Class to return name of category in admin seciton"
        return self.name


class Post(models.Model):
    "Model for creating blog posts"

    class PostManager(models.Manager):
        "Class for filtering posts that are published"
        def get_queryset(self):
            "Class for filtering posts that are published"
            return super().get_queryset().filter(status=1)

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    post_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blogpost', blank=True)
    objects = models.Manager()
    postmanager = PostManager()

    def get_absolute_url(self):
        "Class to return the post_detail url based on the slug name"
        return reverse('BLOG:post_detail', args=[self.slug])

    class Meta:
        "Class to display posts via date created"
        ordering = ['-created_on']

    def like_number(self):
        "Class to display number of likes on a post"
        return self.likes.count()

    def __str__(self):
        "Class to return the post title in admin"
        return self.title


class Comment(models.Model):
    "Model for creating comments"
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        "Class for displaying messages oldest first"
        ordering = ['created_on']

    def __str__(self):
        "Class for showing comments"
        return f'Comment {self.content} by {self.name}'
