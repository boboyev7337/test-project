from django.urls import path
from rest_framework import routers

from account.api.v1.views import UserViewSet
from .views import TestViewSet, CategoryViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'test', TestViewSet)
router.register(r'post', PostViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
]

urlpatterns += router.urls
