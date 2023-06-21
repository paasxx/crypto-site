from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.db.models import Max, Min


from .models import *
import sys
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


table_names = [m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()]

table_class_names = [m.__name__ for c in apps.get_app_configs() for m in c.get_models()]

currencies = [
    i for i in table_names if len(i) <= 5
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

    sd = request.GET.get("startDate")
    ed = request.GET.get("endDate")

    print(crypto.objects.aggregate(Min("date")))

    min_date_table_str = crypto.objects.aggregate(Min("date"))["date__min"]
    max_date_table_str = crypto.objects.aggregate(Max("date"))["date__max"]

    min_date_table = datetime.strptime(min_date_table_str, "%Y-%m-%d %H:%M:%S")
    max_date_table = datetime.strptime(max_date_table_str, "%Y-%m-%d %H:%M:%S")

    if (
        sd == None or ed == None or sd == "" or ed == ""
    ):  # testando erro pra primeira entrada na pag e depois de estar nela com input de data vazio ""
        crypto_data = crypto.objects.all()

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
        }

        return render(request, "app_crypto/crypto_list.html", context)

    else:
        start_date = datetime.strptime(sd, "%Y-%m-%d")
        end_date = datetime.strptime(ed, "%Y-%m-%d")
        crypto_data = crypto.objects.filter(
            date__range=[start_date, end_date]
        ).distinct()

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
        }

        return render(request, "app_crypto/crypto_list.html", context)


def plot(request, crypto):
    context = {"currencies": currencies, "crypto": crypto}

    return render(request, "app_crypto/plot.html", context)
