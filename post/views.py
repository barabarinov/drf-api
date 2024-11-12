from datetime import datetime

from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Like
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: PostSerializer) -> None:
        serializer.save(author=self.request.user)


class LikePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, post_id: int) -> Response:
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            post.likes_count += 1
            post.save()
            return Response({"status": "liked"}, status=status.HTTP_201_CREATED)
        return Response({"status": "already liked"}, status=status.HTTP_400_BAD_REQUEST)


class Analytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        today = datetime.today().date()

        date_from = request.query_params.get("date_from", today.replace(day=1))
        date_to = request.query_params.get("date_to", today)

        likes = (
            Like.objects.filter(created_at__date__range=[date_from, date_to])
            .extra({"day": "date(created_at)"})
            .values("day")
            .annotate(count=Count("id"))
        )
        return Response(likes)
