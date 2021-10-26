from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from api import views

def show(request):
    data = views.get_json(request)
    content = []
    for i in data['data']:
        attributes = { }
        attributes['departure_time'] = i['attributes']['departure_time']
        attributes['status'] = i['attributes']['status']
        trip_id = i['relationships']['trip']['data']['id']
        vehicle_id = ''
        if i['relationships']['vehicle']['data'] is not None:
            vehicle_id = i['relationships']['vehicle']['data']['id']
        
        for x in data['included']:
            if(trip_id == x['id']):
                attributes['destination'] = x['attributes']['headsign']
        
        for y in data['included']:
            if(vehicle_id == y['id']):
                attributes['train'] = y['attributes']['label']
        content.append(attributes)

    template = loader.get_template('board.html')
    return render(request, 'board.html', {'content':content})