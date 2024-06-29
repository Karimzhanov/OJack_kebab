from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )
    email = models.EmailField(
        verbose_name = "Адрес электронной почты"
    )
    password = models.CharField(
        max_length = 255,
        verbose_name = "Пароль"
    )
    confirm_password = models.CharField(
        max_length = 255,
        verbose_name = "Подтверждение пароля"
    )
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"