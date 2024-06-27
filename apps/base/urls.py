from django.urls import path
from apps.base import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
]
