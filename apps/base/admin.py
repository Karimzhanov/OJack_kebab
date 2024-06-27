from django.contrib import admin
from apps.base.models import Home
# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'discription']
