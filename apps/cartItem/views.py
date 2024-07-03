from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import FoodItem, Cart, CartItem, Order
from django.http import JsonResponse
import json

def add_to_cart(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(food_item=food_item, user=request.user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    cart.items.add(cart_item)
    return redirect('cart')

def remove_from_cart(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, food_item=food_item, user=request.user)

    cart.items.remove(cart_item)
    cart_item.delete()
    return redirect('cart')

def cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return render(request, 'cart.html', {'cart': cart})
    else:
        # Handle case where user is not authenticated (optional)
        # For example, redirect them to login page or show a message
        return render(request, 'users/login.html')  # Example of handling not authenticated users

@require_POST
def update_quantity(request, food_id):
    cart_item = get_object_or_404(CartItem, food_item_id=food_id, user=request.user)
    data = json.loads(request.body)
    quantity = data.get('quantity')
    if quantity and quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    return JsonResponse({'success': True})

def checkout(request):
    if request.user.is_authenticated:
        try:
            cart = get_object_or_404(Cart, user=request.user)
            total_price = cart.get_total_price()
            order = Order.objects.create(user=request.user, cart=cart, total_price=total_price)
            cart.items.clear()  # Очищаем корзину после создания заказа
            return render(request, 'checkout.html', {'order': order})
        except Cart.DoesNotExist:
            # Обрабатываем случай, когда корзина пользователя не существует
            return render(request, 'checkout_error.html', {'error_message': 'Ваша корзина пуста или не существует.'})
    else:
        # Обрабатываем случай, когда пользователь не аутентифицирован
        return render(request, 'users/login.html')