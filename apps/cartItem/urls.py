from django.urls import path
from apps.cartItem import views

urlpatterns = [
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:food_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('update_quantity/<int:food_id>/', views.update_quantity, name='update_quantity'),
    path('checkout/', views.checkout, name='checkout'),
]
