from django.shortcuts import render, redirect
from apps.users import models
from django.contrib import messages
from django.contrib.auth import login, authenticate
# Create your views here.
def login(request):
    return render(request, 'users/login.html', locals())

def user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password and username and email:
            user = models.User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user = authenticate(request=request, username=username, email=email, password=password)

            if user:
                login(request, user)

                return redirect('profile', user.id)
    return render(request, 'users/register.html', locals())
        
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = models.User.objects.get(email=email)
        except:
            messages.error(request, 'Пользователь с такой почтой уже существует!')
            return redirect('login')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', user.id)
        else:
            messages.error(request, 'Неправильный или пароль!')
            return redirect('login')
    return render(request, 'users/login.html', locals())


        
    
