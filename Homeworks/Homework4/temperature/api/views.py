from django.http.response import HttpResponse
from django.shortcuts import render
from api.api_processor import API

def index(request):
    return HttpResponse("<h3>Max temperature: {}</h3><h3>Min temperature: {}</h3><h3>Average temperature: {}</h3>".format(API.get_max_temperature(), API.get_min_temperature(), API.get_avg_temperature()))