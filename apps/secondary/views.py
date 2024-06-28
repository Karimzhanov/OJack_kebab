from django.shortcuts import render
from apps.secondary import models
# Create your views here.
def page_not_found(request):
    return render(request, '404.html', locals())

def blog(request):
    news = models.News.objects.all().order_by('?')[:4]
    return render(request, 'blog.html', locals())

def blog_detail(request, id):
    news = models.News.objects.get(id=id)
    return render(request, 'blog-detail.html', locals())

def cart(request):
    return render(request, 'cart.html', locals())

def checkout(request):
    return render(request, 'checkout.html', locals())

def team(request):
    return render(request, 'team.html', locals())

def team_detail(request):
    return render(request, 'team-detail.html', locals())

def gallery(request):
    gallery = models.Gallery.objects.all()
    return render(request, 'gallery.html', locals())

def menu(request):
    return render(request, 'menu.html', locals())

def menu_detail(request):
    return render(request, 'menu-detail.html', locals())

