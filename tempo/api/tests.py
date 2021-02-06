from django.test import TestCase
from django.urls import reverse
import requests
import json


class GetWeatherViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Weather'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather.html')

    def test_view_are_working_with_the_correct_token(self):
        params = {
            'access_key': 'SEU_TOKEN',  # Coloque seu token aqui para testar
            'query': "Barreiras, bahia",
        }
        response = requests.get('http://api.weatherstack.com/current', params)
        resultado = json.loads(response.content)

        context = {}
        context['resultado'] = resultado
        self.assertEqual(resultado['location']['name'], 'Barreiras')

    def test_if_doesnt_work_with_the_wrong_token(self):
        params = {
            'access_key': 'sem token',
            'query': "Barreiras, bahia",
        }
        response = requests.get('http://api.weatherstack.com/current', params)
        resultado = json.loads(response.content)

        context = {}
        context['resultado'] = resultado
        self.assertEqual(resultado['success'], False)

    def test_if_doesnt_work_with_the_wrong_city_name(self):
        params = {
            'access_key': 'SEU_TOKEN',  # Coloque seu token aqui para testar
            'query': "jsdnckjdnckdnscnjsdkjcnkn",
        }
        response = requests.get('http://api.weatherstack.com/current', params)
        resultado = json.loads(response.content)

        context = {}
        context['resultado'] = resultado
        self.assertEqual(resultado['error']['code'], 615)

    def test_if_doesnt_work_with_a_blank_city_name(self):
        params = {
            'access_key': 'SEU_TOKEN',  # Coloque seu token aqui para testar
            'query': "",
        }
        response = requests.get('http://api.weatherstack.com/current', params)
        resultado = json.loads(response.content)

        context = {}
        context['resultado'] = resultado
        self.assertEqual(resultado['error']['code'], 601)
