from django.db import models
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Car

# Create your views here.
PI = 3.14

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    cars = Car.objects.all
    context = {
        'cars':cars,
    }
    template = loader.get_template('cars.html')
    return HttpResponse(template.render(context, request))