import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def read_csv():
    with open(BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


def bus_stations(request):
    data = read_csv()
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(data, 10)
    page = paginator.page(page_number)
    stations_info = page.object_list
    context = {
        'bus_stations': stations_info,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
