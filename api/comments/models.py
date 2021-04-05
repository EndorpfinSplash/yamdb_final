from django.db import models

from ..reviews.models import Review
from ..users.models import User


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='review')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='author')
    text = models.TextField(max_length=500,
                            verbose_name='text')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='publication date')

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
