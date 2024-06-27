from django.shortcuts import render

# Create your views here.
def page_not_found(request):
    return render(request, '404.html', locals())

def blog(request):
    return render(request, 'blog.html', locals())

def blog_detail(request):
    return render(request, 'blog-detail.html', locals())

def cart(request):
    return render(request, 'cart.html', locals())

def checkout(request):
    return

def chef(request):
    return render(request, 'chef.html', locals())

def chef_detail(request):
    return render(request, 'chef-detail.html', locals())

def gallery(request):
    return render(request, 'gallery.html', locals())

def menu(request):
    return render(request, 'menu.html', locals())

def menu_detail(request):
    return render(request, 'menu-detail.html', locals())

