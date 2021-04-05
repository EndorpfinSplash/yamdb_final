from rest_framework import filters, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Genre
from .serializers import GenreSerializer
from ..users.permissions import IsAdminOrReadOnly


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    http_method_names = ['get', 'post', 'delete']
