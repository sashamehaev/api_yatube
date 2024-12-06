from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path
from . import views
from api.views import PostViewSet, CommentViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/\d+/comments', CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', include('djoser.urls')),
    path('api-token-auth/', include('djoser.urls.jwt')),
]
