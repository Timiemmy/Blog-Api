from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
# Create your tests here.

class PotsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="test",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="A trial test for API",
            body="This is a test for the API i created"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A trial test for API")
        self.assertEqual(self.post.body, "This is a test for the API i created")
        self.assertEqual(str(self.post), "A trial test for API")