from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            error_message = "Неверный email или пароль"
    return render(request, 'users/login.html', {'error_message': error_message})

def register(request):
    return render(request, 'users/register.html', locals())