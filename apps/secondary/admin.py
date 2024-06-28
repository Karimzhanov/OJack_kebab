from django.contrib import admin
from apps.secondary import models
# Register your models here.

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date']

@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', ]