from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from posts.models import Post, Group, Comment
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializer import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удалять чужой контент запрещено!')
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    """def get_queryset(self):
        return self.get_post().comments.all()"""

    def get_post(self):
        post_id = self.kwargs
        print(post_id)
        return print('get_object_or_404(Post, pk=post_id)')

    def perform_create(self, serializer):
        self.get_post()
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)
