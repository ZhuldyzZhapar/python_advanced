from django.shortcuts import render, redirect


def index(request):
    # context = {}
    return render(request, 'index.html')


def papers(request):
    # context = {}
    return render(request, 'papers.html')


cars_original = [
    {"id": 1, "name": "Toyota", "color": "gray", "details": {"width": 210, "length": 400}},
    {"id": 2, "name": "Porsche", "color": "red", "details": {"width": 170, "length": 340}},
    {"id": 3, "name": "Mercedes", "color": "brown", "details": {"width": 200, "length": 350}},
    {"id": 4, "name": "Audi", "color": "white", "details": {"width": 210, "length": 400}},
    {"id": 5, "name": "Volkswagen", "color": "blue", "details": {"width": 210, "length": 400}},
]

cars = cars_original.copy()


def cars_view(request):
    extra_div = '<div style="padding: 5px; background-color: yellow">This is an extra div!</div>'
    context = {"username": "Bill Gates", "company": "Microsoft", "cars": cars, "extra": extra_div}
    return render(request, 'cars.html', context)


def cars_restore(request):
    global cars
    cars = cars_original.copy()
    return redirect('/cars/')


def car_view(request, id):
    found_car = None
    for car in cars:
        if car["id"] == id:
            found_car = car
    context = {"car": "Toyota", "id": id, "car": found_car}
    if found_car is None:
        return render(request, 'car_not_found.html')
    return render(request, 'car.html', context)


def car_delete(request, id):

    for car in cars:
        if car["id"] == id:
            cars.remove(car)

    return redirect('/cars/')
