from django.shortcuts import render
import requests
import json
# '7b2f59670991b7510b9a2a0ffacb4fbd'


def get_weather(request):
    search_bar = request.GET.get('search_bar')
    params = {
        'access_key': 'SEU_TOKEN',  # Coloque seu token aqui
        'query': search_bar
    }
    response = requests.get('http://api.weatherstack.com/current', params)
    resultado = json.loads(response.content)

    context = {}
    context['resultado'] = resultado
    return render(request, 'weather.html', context)
