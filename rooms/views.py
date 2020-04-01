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
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "selected_country": country,
        "selected_room_type": room_type,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
    }

    return render(request, "rooms/search.html", {**form, **choices},)
