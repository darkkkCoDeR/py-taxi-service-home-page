from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.count()
    num_manufactures = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    return render(request, "base.html", {"num_drivers": num_drivers, "num_manufactures": num_manufactures, "num_cars": num_cars})
