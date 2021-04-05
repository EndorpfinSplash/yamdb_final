from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    slug = models.SlugField(unique=True, verbose_name='slug')

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name
