from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "author", "content", "created_at", "likes_count")
        read_only_fields = ("id", "author", "created_at", "likes_count")
