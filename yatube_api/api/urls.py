from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from api.views import PostList


# router = routers.DefaultRouter()
# router.register('posts/', PostAPI.as_view())
# router.register('groups', GroupViewSet)
# router.register(r'posts/(?P<post_id>\d)/comments')
# router.register(r'posts/(?P<post_id>\d)/comments/(?P<comment_id>\d)')
# router.register('posts/<int:post_id>/comments', UserViewSet)
# router.register('posts/<int:post_id>/comments/<int:comment_id>', UserViewSet)
# router.register('groups', AchievementViewSet)

urlpatterns = [
    path('posts/', PostList.as_view()),
    # path('cats/<int:pk>/', CatDetail.as_view()),
    # path('', include(router.urls)),
    path('api-token-auth/', include('djoser.urls')),
    path('api-token-auth/', include('djoser.urls.jwt')),
]
