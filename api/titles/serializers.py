from rest_framework import serializers

from .models import Title
from ..categories.models import Category
from ..genres.models import Genre


class RepresentationField(serializers.SlugRelatedField):
    def to_representation(self, value):
        return {'name': value.name, 'slug': value.slug}


class TitleSerializer(serializers.ModelSerializer):
    category = RepresentationField(slug_field='slug',
                                   queryset=Category.objects.all()
                                   )
    genre = RepresentationField(slug_field='slug',
                                queryset=Genre.objects.all(),
                                many=True
                                )

    class Meta:
        fields = '__all__'
        model = Title


class TitleListRetrieveSerializer(TitleSerializer):
    rating = serializers.IntegerField(read_only=True)
