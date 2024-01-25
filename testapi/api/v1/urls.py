from django.urls import path
from rest_framework import routers

from account.api.v1.views import UserViewSet
from .views import TestViewSet, CategoryViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet, name='user')
router.register(r'test', TestViewSet, name='test')
router.register(r'post', PostViewSet, name='post')
router.register(r'category', CategoryViewSet, name='category')

urlpatterns = [
]

urlpatterns += router.urls
