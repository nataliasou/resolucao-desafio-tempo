from django.shortcuts import render
import requests
import json



def get_weather(request):
    """
        This function receives the data from the form and use it to access the Wheatherstack's API.
        It returns a dictionary with all the information that the API have.

        **Template:**
        :template:'api/templates/weather.html'
        """
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
