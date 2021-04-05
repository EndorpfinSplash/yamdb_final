from django.db.models import Avg
from rest_framework import viewsets

from .models import Title
from .filters import TitleFilter
from .serializers import TitleSerializer, TitleListRetrieveSerializer
from ..users.permissions import IsAdminOrReadOnly


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleListRetrieveSerializer
        return super().get_serializer_class()
