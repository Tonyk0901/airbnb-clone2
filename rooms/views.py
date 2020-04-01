from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django_countries import countries
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):
    """ Home View Definitino """

    model = models.Room
    context_object_name = "rooms"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


class RoomDetail(DetailView):
    """ Room Detail View Definitino """

    model = models.Room


def search(request):
    city = str.capitalize(request.GET.get("city", "Anywhere"))
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))

    price = int(request.GET.get("price", 1))
    guests = int(request.GET.get("guests", 1))
    bedrooms = int(request.GET.get("bedrooms", 1))
    beds = int(request.GET.get("beds", 1))
    baths = int(request.GET.get("baths", 1))
    instant = request.Get.get("instant", False)
    super_host = request.Get.get("super_host", False)

    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    form = {
        "city": city,
        "selected_country": country,
        "selected_room_type": room_type,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(request, "rooms/search.html", {**form, **choices},)
