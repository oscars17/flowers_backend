from django.db import models
from text_materials.models import Article
from django.utils import timezone


class HeaderImage(models.Model):
    image = models.ImageField(
        upload_to='static/images/',
        verbose_name='article image',
    )
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        verbose_name='article',
        related_name='header_image'
    )
    date = models.DateTimeField(
        default=timezone.now,
        verbose_name='date created'
    )

    def __str__(self):
        return 'Header image of {0}'.format(self.article)
