from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d)/comments', CommentViewSet)
# router.register('posts/<int:post_id>/comments', UserViewSet)
# router.register('posts/<int:post_id>/comments/<int:comment_id>', UserViewSet)
# router.register('groups', AchievementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', include('djoser.urls')),
    path('api-token-auth/', include('djoser.urls.jwt')),
]
