from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikePost, Analytics

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<int:post_id>/like/", LikePost.as_view(), name="like_post"),
    path("analytics/", Analytics.as_view(), name="analytics"),
]
