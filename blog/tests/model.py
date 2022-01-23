from django.test import TestCase
from blog.models import Comment


class TestBlogModels(TestCase):
    "Test for returning self via name"
    def test_mode_str(self):
        name = Comment.objects.create(name='test')
        content = Comment.objects.create(content='Test for content')
        self.assertEqual(str(name), 'test')
