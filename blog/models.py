"Models page for blog"
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Post model directly from Django Central

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    "Model for creating blog posts"
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)

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
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    active = models.BooleanField(default=False)

    class Meta:
        "Class for displaying messages oldest first"
        ordering = ['created_on']

    def __str__(self):
        "Class for showing comments"
        return f'Comment {self.content} by {self.name}'