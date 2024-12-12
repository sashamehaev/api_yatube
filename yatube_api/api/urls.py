from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path
from api.views import PostViewSet, CommentViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/\d+/comments', CommentViewSet, basename='comment')
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
