from django.contrib import admin
from .models import FoodItem, CartItem, Cart, Order

@admin.register(FoodItem)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price' ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' ]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'food_item', 'quantity' ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cart', 'created_at' ]
