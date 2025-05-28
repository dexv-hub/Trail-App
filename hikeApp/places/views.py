from django.shortcuts import render

from .models import Place


def locations(request):
    places = Place.objects.all()
    return render(request, 'main/index.html', {'places': places})

