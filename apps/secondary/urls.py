from django.urls import path
from apps.secondary import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

]
