from django.contrib import admin
from apps.users import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']
    