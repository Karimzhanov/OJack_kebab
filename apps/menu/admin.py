from django.contrib import admin
from apps.menu.models import MenuItem
 
# Register your models here.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', ]