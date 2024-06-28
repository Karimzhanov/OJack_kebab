from django.shortcuts import render
from apps.base import models
# Create your views here.
def index(request):
    user = models.Home.objects.latest('id')
    return render(request, 'base/index.html', locals())

def about(request):
    about = models.About.objects.latest('id')
    team = models.Team.objects.all()
    teamworks = models.TeamWorks.objects.all()
    testimonial = models.Testimonial.objects.all()
    return render(request, 'base/about.html', locals())


