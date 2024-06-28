from django.shortcuts import render
from apps.users import models
# Create your views here.
def login(request):
    return render(request, 'users/login.html', locals())

def register(request):
    register = models.Register.objects.get
    return render(request, 'users/register.html', locals())