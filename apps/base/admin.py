from django.contrib import admin
from apps.base import models
# Register your models here.
@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', ]

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'profession','facebook', 'twitter', 'email', 'instagram']

@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession']