from django.shortcuts import render
from places.models import Place

def index(request):
    places = Place.objects.all()
    return render(request, 'main/index.html', {'places': places})

def about(request):
    return render(request, 'main/about.html')

