from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime


from .models import *
import sys
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


tables = [m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()]

table_class_names = [m.__name__ for c in apps.get_app_configs() for m in c.get_models()]

currencies = [
    i for i in tables if len(i) <= 5
]  # Selecting only names of tickers with less than 4 digits

class_names = [i for i in table_class_names if len(i) <= 5]


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

    start_date = None
    end_date = None

    if start_date == None or end_date == None:
        crypto_data = crypto.objects.all()

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
        }

        return render(request, "app_crypto/crypto_list.html", context)

    else:
        sd = request.GET.get("startDate")
        ed = request.GET.get("endDate")
        start_date = datetime.strptime(sd, "%Y-%m-%d")
        end_date = datetime.strptime(ed, "%Y-%m-%d")

        crypto_data = crypto.objects.filter(date=[start_date, end_date]).distinct()

        return render(request, "app_crypto/crypto_list.html", context)


def plot(request, crypto):
    context = {"currencies": currencies, "crypto": crypto}

    return render(request, "app_crypto/plot.html", context)
