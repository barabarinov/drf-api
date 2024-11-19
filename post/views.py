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

DATE_FORMAT = "%Y-%m-%d"


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
        default_date_from = today.replace(day=1).strftime(DATE_FORMAT)
        default_date_to = today.strftime(DATE_FORMAT)

        date_from = request.query_params.get("date_from", default_date_from)
        date_to = request.query_params.get("date_to", default_date_to)

        try:
            date_from = datetime.strptime(date_from.strip(), DATE_FORMAT).date()
            date_to = datetime.strptime(date_to.strip(), DATE_FORMAT).date()
        except ValueError:
            return Response(
                {
                    "error": "Invalid date format. Both 'date_from' and 'date_to' must be in YYYY-MM-DD format."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if date_from > date_to:
            return Response(
                {"error": "date_from cannot be later than date_to."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        likes = (
            Like.objects.filter(created_at__date__range=[date_from, date_to])
            .extra({"day": "date(created_at)"})
            .values("day")
            .annotate(count=Count("id"))
        )
        return Response(likes)
