from django.urls import path
from apps.menu import views

urlpatterns = [
    path('menu/', views.menu, name = 'menu'),
    path('menu-detail/', views.menu_detail, name = 'menu_detail'),
]