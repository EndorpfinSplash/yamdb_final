from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from ..users.permissions import IsStaffOrAuthorOrReadOnly
from .serializers import CommentSerializer
from .models import Review


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsStaffOrAuthorOrReadOnly,)

    def get_queryset(self, *args, **kwargs):
        review = get_object_or_404(Review,
                                   pk=self.kwargs.get('review_id'),
                                   title_id=self.kwargs.get('title_id'),
                                   )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review,
                                   pk=self.kwargs.get('review_id'),
                                   title_id=self.kwargs.get('title_id'),
                                   )
        serializer.save(author=self.request.user, review=review)
