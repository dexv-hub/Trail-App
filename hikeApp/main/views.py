from http.client import responses
from django.shortcuts import render
from places.models import Place
import requests, pprint, json

def index(request):
    places = Place.objects.all()
    return render(request, 'main/index.html', {'places': places})

def about(request):
    return render(request, 'main/about.html')

def weather_view(request):
    api_key = 'nwwE6BN6rw09wyzmWzGEOQNNu4GubspE'
    location = 'London'
    latitude = 51.5074
    longitude = -0.1278
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&timesteps=1d&apikey=nwwE6BN6rw09wyzmWzGEOQNNu4GubspE'

    response = requests.get(url)
    data = response.json()

    print(json.dumps(data, indent=2))

    daily_forecast = data.get('timelines', {}).get('daily', [])

    return render(request, 'main/weather.html', {'forecasts': daily_forecast})