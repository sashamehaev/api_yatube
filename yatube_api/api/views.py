from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from posts.models import Post, Group, Comment
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


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # queryset во вьюсете не указываем
    # Нам тут нужны не все комментарии, а только связанные с котом с id=cat_id
    # Поэтому нужно переопределить метод get_queryset и применить фильтр

    def get_queryset(self):
        # Получаем id котика из эндпоинта
        cat_id = self.kwargs.get("cat_id")
        # И отбираем только нужные комментарии
        new_queryset = Comment.objects.filter(cat=cat_id)
        return new_queryset
