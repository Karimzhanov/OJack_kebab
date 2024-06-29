from django.contrib import admin
from apps.users import models

# Register your models here.
@admin.register(models.Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']
    