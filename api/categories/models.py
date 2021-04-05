from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    slug = models.SlugField(unique=True, verbose_name='slug')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
