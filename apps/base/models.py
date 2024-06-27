from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Главная страница"
    )

    image = models.ImageField(
        upload_to = "info_users",
        verbose_name = "Задний Фон"
    )  

    description = models.TextField(
        max_length = 255,
        verbose_name = "описания заговка"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = " Главная страницы"

class About(models.Model):
    description = models.TextField(
        max_length = 255,
        verbose_name = "Описание"
    )
    subdescription = models.TextField(
        max_length = 255,
        verbose_name = "Подописание"
    )
    image = models.ImageField(
        upload_to = "image_about/",
        verbose_name = "Изображение"
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Team(models.Model):
    fullname = models.CharField(
        max_length = 255,
        verbose_name = "Полное имя"
    )
    photo = models.ImageField(
        upload_to = "photo_employee/",
        verbose_name = "Фотография"
    )
    profession = models.CharField(
        max_length = 255,
        verbose_name = 'Профессия'
    )
    facebook = models.URLField(
        max_length = 255,
        verbose_name = 'Facebook'
    )
    twitter = models.URLField(
        max_length = 255,
        verbose_name = 'Twitter'
    )
    email = models.EmailField(
        max_length = 255,
        verbose_name = 'Почта'
    )
    instagram = models.URLField(
        max_length = 255,
        verbose_name = 'Instagram'
    )

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class Testimonial(models.Model):
    photo = models.ImageField(
        upload_to = "testimonial/",
        verbose_name = "Фотография"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    profession = models.CharField(
        max_length = 255,
        verbose_name = 'Профессия'
    )
    comment = models.TextField(
        max_length = 255,
        verbose_name = 'Комментарий'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'