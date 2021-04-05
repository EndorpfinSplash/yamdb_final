from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import Review, Title
from ..users.permissions import IsStaffOrAuthorOrReadOnly
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsStaffOrAuthorOrReadOnly,)

    def get_queryset(self, *args, **kwargs):
        return Review.objects.filter(title__id=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def perform_update(self, serializer):
        serializer.save()
