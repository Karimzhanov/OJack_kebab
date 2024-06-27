from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Главная страница"
    )


    image = models.ImageField(
        upload_to= "info_users",
        verbose_name= "Задний Фон"
    )  

    discription = models.TextField(
        max_length=255,
        verbose_name="описания заговка"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = " Главная страницы"
