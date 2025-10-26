from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'yzJourney/index.html', {'journeys': journeys})
def about_me(request):
    abouts = AboutMe.objects.all()
    return render(request, 'yzJourney/aboutMe.html', {'abouts': abouts})
