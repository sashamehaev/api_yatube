from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from posts.models import Post, Group, Comment
from .serializer import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Получаем id котика из эндпоинта
        post_id = self.kwargs.get("post_id")
        # И отбираем только нужные комментарии
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset
