from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models

from ..categories.models import Category
from ..genres.models import Genre


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='category')
    genre = models.ManyToManyField(Genre,
                                   verbose_name='genre')
    name = models.CharField(max_length=150, verbose_name='name')
    year = models.IntegerField(
        validators=(MaxValueValidator(date.today().year),),
        verbose_name='year')
    description = models.TextField(max_length=150,
                                   verbose_name='description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'title'
        verbose_name_plural = 'titles'
