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
            f"<Post(id={self.id}, author={self.author.username}, "
            f"content={self.content[:20]!r}, likes_count={self.likes_count}, "
            f"created_at={self.created_at})>"
        )

    def __str__(self) -> str:
        return f"Post by {self.author.username} ({self.likes_count} likes): {self.content[:15]}..."


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return (
            f"<Like(id={self.id}, user={self.user.username}, post_id={self.post.id}, "
            f"created_at={self.created_at})>"
        )

    def __str__(self) -> str:
        return f"Like by {self.user.username} on Post ID {self.post.id}"
