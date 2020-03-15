from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Currency

# Create your views here.
def index(request):
    req = (requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")).json()
    currencies = []

    for i in req:
        c = Currency()
        c.name = i['ccy']
        c.buy = i['buy']
        c.sale = i['sale']
        currencies.append(c)

    return render(request, 'rates.html', {'currencies' : currencies})