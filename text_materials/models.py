from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings


class ArticleManager(models.Manager):
    def slider_preview(self):
        return super().get_queryset().order_by('date')[:6]


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='slug'
    )
    text = models.TextField(verbose_name='text')
    date = models.DateTimeField(default=timezone.now, verbose_name='date created')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='user',
        on_delete=models.CASCADE
        )
    important = models.BooleanField(
        default=False,
        verbose_name='important status'
    )
    objects = ArticleManager()

    def __str__(self):
        return self.title + ' article'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
