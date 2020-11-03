from django.shortcuts import render, redirect
from pizza.models import Car
from pizza.models import Color
import random

def index(request):
    # context = {}
    return render(request, 'index.html')


def papers(request):
    # context = {}
    return render(request, 'papers.html')


def cars_view(request):
    filter = ""
    if request.method == "POST":
        print("Something is posted!")
        print(request.POST)
        filter = request.POST.get("search","")

    extra_div = '<div style="padding: 5px; background-color: yellow">This is an extra div!</div>'

    cars = Car.objects.all()
    if filter != "":
        cars = Car.objects.filter(color__name__contains=filter) | Car.objects.filter(name__contains=filter)

    for i in range(len(cars)):
        if i % 3 == 0:
            cars[i].active = "ACTIVE"
        else:
            cars[i].active = ""

    context = {"username": "Bill Gates", "company": "Microsoft", "cars": cars, "extra": extra_div}
    return render(request, 'cars.html', context)


def cars_add(request):
    default_car = Car()
    default_car.name = "Toyota"
    default_car.width = 200
    default_car.length = 350
    default_car.color = Color.objects.all().first()

    context = {"colors": Color.objects.all(),
               "default": default_car}
    if request.method == "POST":
        car = Car()
        car.name = request.POST.get("brand","")
        car.length = int(request.POST.get("length","0"))
        car.width = int(request.POST.get("width","0"))
        car.color = Color.objects.get(id=int(request.POST.get("color", "0")))
        context["default"] = car
        if car.name == "":
            context["error"] = "Please enter any name"
        elif car.length > 400 or car.length < 100:
            context["error"] = "Please enter correct length"
        else:
            car.save()
            return redirect("/cars/")

    return render(request, 'cars_add.html', context)


def cars_add_random(request):
    colors = Color.objects.all()
    color = colors[random.randint(0,len(colors)-1)]
    car_brands = ["Toyota", "Mercedes", "Porsche", "Audi", "Volkswagen", "Lexus", "KIA"]
    name = car_brands[random.randint(0,len(car_brands)-1)]
    car = Car()
    car.name = name
    car.color = color
    car.save()
    return redirect('/cars/')


def car_view(request, id):
    try:
        car = Car.objects.get(id=id)
        context = {"car": car}
    except:
        return render(request, 'car_not_found.html')
    return render(request, 'car.html', context)


def car_delete(request, id):
    Car.objects.filter(id=id).delete()
    return redirect('/cars/')
