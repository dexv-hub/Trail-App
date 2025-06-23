from http.client import responses
from django.shortcuts import render
from places.models import Place
import requests, pprint, json
from datetime import datetime

def about(request):
    return render(request, 'main/about.html')

def index(request):
    #api_key = 'nwwE6BN6rw09wyzmWzGEOQNNu4GubspE'
    #location = 'London'
    # latitude = 51.5074
    #longitude = -0.1278
    # url = f'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&timesteps=1d&apikey=nwwE6BN6rw09wyzmWzGEOQNNu4GubspE'

    #response = requests.get(url)
    #data = response.json()

    #print(json.dumps(data, indent=2))

    #daily_forecast = data.get('timelines', {}).get('daily', [])

    daily_forecast = []



    places = Place.objects.all()

    return render(request, 'main/index.html',{'forecasts': daily_forecast, 'places': places })