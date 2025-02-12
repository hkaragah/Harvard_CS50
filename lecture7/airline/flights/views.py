
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Flight


# Create your views here.
def index(request):
    # return HttpResponse("Flights")
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist: # Special exception raised by Django when a query returns no results
        raise Http404("Flight not found.")
    context = {
        "flight": flight
    }
    return render(request, "flights/flight.html", context)
