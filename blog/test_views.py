from django.test import TestCase


class TestViews(TestCase):
    "Basic testing for content location"
    def test_homepage(self):
        "Test for finding homepage where it is expected"
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('BLOG/base.html')

    def test_view_url_exists_at_desired_location(self):
        "Test for news.html page in right place"
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location2(self):
        "Test for create.html page in right place"
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)
