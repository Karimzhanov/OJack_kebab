from django.shortcuts import render
from apps.base.models import Home
# Create your views here.
def index(request):
    user = Home.objects.latest('id')
    return render(request, 'base/index.html', locals())

def about(request):
    return render(request, 'base/about.html', locals())

def contact(request):
    return render(request, 'base/contact.html', locals())

