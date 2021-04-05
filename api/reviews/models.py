from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from ..titles.models import Title
from ..users.models import User


class Review(models.Model):
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='title')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='author')
    text = models.TextField(max_length=500,
                            verbose_name='text')
    score = models.IntegerField(default=0,
                                validators=(MinValueValidator(1),
                                            MaxValueValidator(10)),
                                verbose_name='score')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='publication date')

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
