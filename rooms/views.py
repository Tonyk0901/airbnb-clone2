from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):
    """ Home View Definitino """

    model = models.Room
    context_object_name = "rooms"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404


class RoomDetail(DetailView):
    """ Room Detail View Definitino """

    model = models.Room


def search(request):
    city = str.capitalize(request.GET.get("city"))
    return render(request, "rooms/search.html", {"city": city})
