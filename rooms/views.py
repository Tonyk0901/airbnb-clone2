from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django_countries import countries
from django.shortcuts import render, redirect
from . import models, forms


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
    form = forms.SearchForm(request.GET)
    return render(request, "rooms/search.html", {"form": form},)
