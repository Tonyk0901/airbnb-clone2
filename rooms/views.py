from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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


class SearchView(View):
    def get(self, request):
        country = request.GET.get("country")
        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for facility in facilities:
                    filter_args["facilities"] = facility

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 1, orphans=1)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                get_copy = request.GET.copy()
                address = get_copy.urlencode()

                return render(
                    request,
                    "rooms/search.html",
                    {"form": form, "rooms": rooms, "address": address},
                )

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})
