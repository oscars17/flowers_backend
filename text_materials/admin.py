from django.contrib import admin
from . import models
from files.models import HeaderImage


class HeaderImageInline(admin.TabularInline):
    model = HeaderImage


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    fields = ('title', 'text', 'user', 'important')
    list_display = ('title', 'date', 'user', 'important')
    inlines = [
        HeaderImageInline
    ]
