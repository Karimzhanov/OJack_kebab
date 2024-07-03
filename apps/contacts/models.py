from django.db import models

# Create your models here.

class Contacts(models.Model):
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Номер телефона "
    )
    our_location  = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Почта "
    )
    opening_hours = models.CharField(
        max_length=255,
        verbose_name="Время работы"
    )
    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = " Контакты"


class Contact(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name = 'Почта',
    )
    number = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    subject = models.TextField(
        verbose_name= 'Тема'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name='Сообщение'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

class Reservation(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта' 
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Номер телефона'
    )
    date = models.DateField(
        verbose_name='Дата бронирования'
        )
    time = models.TimeField(
        verbose_name='Время бронирования'
    )
    num_people = models.IntegerField(
        verbose_name='Количество человек'
        )

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

class Reservatio(models.Model):
    image1 = models.ImageField(
        upload_to = "info_users/",
        verbose_name = "Задний Фон"
    )


    image = models.ImageField(
        upload_to = "info_users",
        verbose_name = "фото"
    )
    def __str__(self):
        return f'Изображение {self.image}'

    class Meta:
        verbose_name = "страница для Бронирование "
        verbose_name_plural = "страница для Бронирование"