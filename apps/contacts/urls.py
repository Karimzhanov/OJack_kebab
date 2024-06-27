from django.urls import path
from apps.contacts import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
  

]
