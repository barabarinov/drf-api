from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)

    def __repr__(self) -> str:
        return (
            f"Post(id={self.id}, content={self.content[:20]}, likes={self.likes_count})"
        )

    def __str__(self) -> str:
        return f"Post: {self.content[:15]} by {self.author} with {self.likes_count} likes"


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return (
            f"Like(id={self.id}, "
            f"user={self.user_id}, "
            f"post={self.post.id}, "
            f"created_at={self.created_at})"
        )
