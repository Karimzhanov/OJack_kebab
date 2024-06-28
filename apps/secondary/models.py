from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок новости"
    )
    image = models.ImageField(
        upload_to="news",
        verbose_name="Изображение новости"
    )
    content = RichTextField(
        verbose_name="Содержание новости"
    )
    content2 = RichTextField(
        verbose_name="Содержание новости 2",
        blank=True, null=True
    )
    content3 = RichTextField(
        verbose_name="Содержание новости 3",
        blank=True, null=True
    )
    content4 = RichTextField(
        verbose_name="Содержание новости 4",
        blank=True, null=True
    )
    date = models.DateField(
        verbose_name="Дата публикации"
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор поста'
    )

    def __str__(self):
        return f'{self.author} опубликовал новость {self.title}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Gallery(models.Model):
    image = models.ImageField(
        upload_to="gallery/",
        verbose_name="Изображение галереи"
    )

    def __str__(self):
        return f'Изображение {self.image}'
    
    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Изображения галереи'