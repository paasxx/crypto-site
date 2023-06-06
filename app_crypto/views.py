from django.shortcuts import render

from .models import *
import sys
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


tables = [m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()]

table_class_names = [m.__name__ for c in apps.get_app_configs() for m in c.get_models()]

currencies = [
    i for i in tables if len(i) <= 4
]  # Selecting only names of tickers with less than 4 digits

class_names = [i for i in table_class_names if len(i) <= 4]


# Create your views here.


def home(request):
    context = {
        "currencies": currencies,
        "class_names": class_names,
    }
    return render(request, "app_crypto/home.html", context)


def market(request, crypto):
    crypto_name = crypto

    crypto = getattr(sys.modules[__name__], crypto)

    crypto_data = crypto.objects.all()

    context = {
        "currencies": currencies,
        "crypto": crypto_name,
        "crypto_data": crypto_data,
    }
    return render(request, "app_crypto/crypto_list.html", context)


def plot(request, crypto):
    context = {"currencies": currencies, "crypto": crypto}

    return render(request, "app_crypto/plot.html", context)
