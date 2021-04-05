from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Comment


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
