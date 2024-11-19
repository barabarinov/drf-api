from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Like


class AnalyticsTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )

        response = self.client.post(
            reverse("user:token_obtain_pair"),
            data={"username": "testuser", "password": "password"},
        )
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.posts = [
            Post.objects.create(author=self.user, content=f"Test Post {i}")
            for i in range(1, 10)
        ]

        today = date.today()
        dates = [today - timedelta(days=i) for i in range(3)]

        for i, post in enumerate(self.posts):
            like_date = dates[i // 3]
            Like.objects.create(user=self.user, post=post, created_at=like_date)

    def test_analytics_with_valid_date_range(self):
        url = (
            reverse("post:analytics")
            + f"?date_from={date.today() - timedelta(days=3)}&date_to={date.today()}"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("day", response.data[0])
        self.assertIn("count", response.data[0])

    def test_analytics_with_invalid_date_format(self):
        url = reverse("post:analytics") + "?date_from=invalid-date&date_to=invalid-date"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_analytics_without_date_range(self):
        url = reverse("post:analytics")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
