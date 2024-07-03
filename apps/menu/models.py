from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
        
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=5, 
        verbose_name="Цена"
        )
    
    description = models.TextField(
        verbose_name="Описание блюда"
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
