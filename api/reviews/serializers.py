from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    ValidationError,
)

from .models import Review


class ReviewSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date',)

    def validate(self, attrs):
        request = self.context.get('request')
        if request.method == 'POST':
            if Review.objects.filter(
                    title=self.context.get('view').kwargs.get('title_id'),
                    author=request.user).exists():
                raise ValidationError('Review already exists')
        return attrs
