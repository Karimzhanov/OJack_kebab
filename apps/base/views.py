from django.shortcuts import render
from apps.base import models
from apps.menu.models import MenuItem


# Create your views here.
def index(request):
    user = models.Home.objects.latest('id')
    team = models.Team.objects.all()
    about = models.About.objects.latest('id')
    menu_items = MenuItem.objects.all().order_by('-id')[:8]  # Получаем 8 последних добавленных элементов
    return render(request, 'base/index.html', locals())

def about(request):
    about = models.About.objects.latest('id')
    team = models.Team.objects.all()
    testimonial = models.Testimonial.objects.all()
    return render(request, 'base/about.html', locals())


