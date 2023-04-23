from django.urls import path, include
from rest_framework import routers

from friendlyface.views import (
    PostViewSet,
    TagViewSet,
    ProfileViewSet,
)

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("tags", TagViewSet)
router.register("profiles", ProfileViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "friendlyface"
