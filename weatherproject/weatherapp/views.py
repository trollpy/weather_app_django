from django.shortcuts import render
# Create your views here.
import requests
import json
import datetime  # Add this import
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import CityForm
from .models import City

def index(request):
    form = CityForm()
    weather_data = None
    error_message = None
    forecast_data = None  # Add this line
   
    api_key = getattr(settings, 'OPENWEATHERMAP_API_KEY', None)
    if not api_key or api_key == '':
        error_message = "API key is not set or is invalid. Please check your settings."
        return render(request, 'weatherapp/index.html', {
            'form' : form,
            'error_message': error_message,
            'recent_searches' : []
        })
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
           
            # Save to history
            City.objects.create(name=city_name)
           
            # Call OpenWeatherMap API
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={settings.OPENWEATHERMAP_API_KEY}'
           
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise exception for HTTP errors
               
                weather_data = response.json()
                
                # ADD FORECAST CODE HERE - START
                # Get forecast data
                forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={settings.OPENWEATHERMAP_API_KEY}'
                
                try:
                    forecast_response = requests.get(forecast_url)
                    forecast_response.raise_for_status()
                    
                    forecast_data_raw = forecast_response.json()
                    
                    # Process forecast data (get one forecast per day)
                    processed_forecast = []
                    date_set = set()
                    
                    for item in forecast_data_raw.get('list', []):
                        date = item['dt_txt'].split(' ')[0]
                        # Only take the first forecast for each day
                        if date not in date_set and len(processed_forecast) < 5:
                            date_set.add(date)
                            processed_forecast.append({
                                'date': datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%a'),  # Day name
                                'temp': round(item['main']['temp']),
                                'description': item['weather'][0]['description'],
                                'icon': item['weather'][0]['icon']
                            })
                    
                    forecast_data = processed_forecast
                except requests.RequestException:
                    # If forecast fails, we'll just leave forecast_data as None
                    pass
                # ADD FORECAST CODE HERE - END
                
            except requests.RequestException:
                error_message = "Could not retrieve weather data. Please try again."
   
    # Get the 5 most recent searches
    recent_searches = City.objects.order_by('-searched_at')[:5]
   
    context = {
        'form': form,
        'weather_data': weather_data,
        'error_message': error_message,
        'recent_searches': recent_searches,
        'forecast_data': forecast_data  # Add this line
    }
   
    return render(request, 'weatherapp/index.html', context)
