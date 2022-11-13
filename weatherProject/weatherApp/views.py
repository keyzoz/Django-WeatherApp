from django.shortcuts import render

# Create your views here.

import urllib.request
import json

def index(request):
    if request.method == 'POST':
        TOKEN = "YOUR_TOKEN"
        city = request.POST['city']
        sourse = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + 
                                        city + f'&units=metric&appid={TOKEN}').read()
        list_of_data = json.loads(sourse)
            
        data = {
            "country_code" : str(list_of_data['sys']['country']),
            "temp" : str(list_of_data['main']['temp']) + ' °C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "main" : str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon" : str(list_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data = {}
    
    return render(request, "main/index.html", data)