from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html', locals())

def about(request):
    return render(request, 'base/about.html', locals())

def contact(request):
    return render(request, 'base/contact.html', locals())