from django.shortcuts import HttpResponse
from pizza.models import Car
import json


def numbers(request):
    our_stats = [500, 400, 300, 400, 500, 700,
                 800, 900, 900, 0, 1100, 1200]
    return HttpResponse(json.dumps(our_stats))


def cars(request):
    our_cars = []
    for car in Car.objects.all():
        our_cars.append({
            "name": car.name,
            "id": car.id,
            "color": car.color.name,
        })

    return HttpResponse(json.dumps(our_cars))

