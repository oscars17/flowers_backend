from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name='slug')
    text = models.TextField(verbose_name='text')
    created = models.DateTimeField(default=timezone.now, verbose_name='created')
    user = models.ForeignKey(settings.AUT_USER_MODEL,
                             verbose_name='user',
                             on_delete=models.CASCADE
                             )

    def __str__(self):
        return self.title + ' article'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
