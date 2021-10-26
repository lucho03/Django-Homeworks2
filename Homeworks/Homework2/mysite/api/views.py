from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import requests

def get_json(request):
    url = 'https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north'
    url2 = 'https://api-v3.mbta.com/predictions?filter[stop]=place-north'
    url3 = 'https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=vehicle%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north'
    r = requests.get(url3, headers={'Content-type': 'application/json'})
    json_data = r.json()
    return json_data