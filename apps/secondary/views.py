from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html', locals())

def login(request):
    return render(request, 'login.html', locals())