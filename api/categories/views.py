from rest_framework import filters, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Category
from .serializers import CategorySerializer
from ..users.permissions import IsAdminOrReadOnly


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    http_method_names = ['get', 'post', 'delete']
