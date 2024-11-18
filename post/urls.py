from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikePost, Analytics

router = DefaultRouter()
router.register("posts", PostViewSet)

app_name = "post"

urlpatterns = [
    path("posts/analytics/", Analytics.as_view(), name="analytics"),
    path("posts/<int:post_id>/like/", LikePost.as_view(), name="like_post"),
    path("", include(router.urls)),
]
