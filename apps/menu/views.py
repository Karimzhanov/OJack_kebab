from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def menu(request):
    menu = MenuItem.objects.latest('id')
    return render(request, 'menu.html', locals())


def menu_detail(request):
    return render(request, 'menu-detail.html', locals())    