from django.urls import path
from apps.users import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register')
]
