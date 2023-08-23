from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from .forms import *
from .yfinanceAPI import *
from .plots import *
from .models import *


currencies = getTablesNames()
class_names = getModelsNames()


def home(request):
    context = {
        "currencies": currencies,
        "class_names": class_names,
    }

    updateDatabase(assets, request)

    return render(request, "app_crypto/home.html", context)


def market(request, crypto):
    crypto_name = crypto
    crypto_model = getModelByName(crypto)
    min_date_table = crypto_model.crypto_objects.first_date().date
    max_date_table = crypto_model.crypto_objects.last_date().date
    crypto_data_all = list(crypto_model.crypto_objects.all_data().values())

    context = {
        "currencies": currencies,
        "crypto": crypto_name,
        "min_date_table": min_date_table,
        "max_date_table": max_date_table,
    }

    if request.method == "POST":
        sd = request.POST["startDate"]
        ed = request.POST["endDate"]

        ## Tentar colocar essa logica em um form

        first_error = sd == "" or ed == ""

        second_error = (
            datetime.strptime(ed, "%Y-%m-%d") < datetime.strptime(sd, "%Y-%m-%d")
            if not first_error
            else False
        )

        if first_error or second_error:
            if first_error:
                messages.warning(request, "Fill all Date fields before Search!")
            else:
                messages.warning(
                    request,
                    "End Date must be greater than Start Date, Please try again.",
                )
            crypto_data = crypto_data_all
            context["crypto_data"] = crypto_data
            return render(request, "app_crypto/crypto_list.html", context)

        else:
            crypto_data = list(
                crypto_model.crypto_objects.between_dates(
                    datetime.strptime(sd, "%Y-%m-%d"),
                    datetime.strptime(ed, "%Y-%m-%d"),
                ).values()
            )

            context["crypto_data"] = crypto_data
            return render(request, "app_crypto/crypto_list.html", context)

    else:
        crypto_data = crypto_data_all
        context["crypto_data"] = crypto_data
        return render(request, "app_crypto/crypto_list.html", context)


def plot(request, crypto):
    crypto_name = crypto
    crypto_model = getModelByName(crypto)
    min_date_table = crypto_model.crypto_objects.first_date().date
    max_date_table = crypto_model.crypto_objects.last_date().date
    crypto_data_all = crypto_model.crypto_objects.all_data()

    context = {
        "currencies": currencies,
        "crypto": crypto_name,
        "min_date_table": min_date_table,
        "max_date_table": max_date_table,
    }

    if request.method == "POST":
        sd = request.POST["startDate"]
        ed = request.POST["endDate"]

        first_error = sd == "" or ed == ""

        second_error = (
            datetime.strptime(ed, "%Y-%m-%d") < datetime.strptime(sd, "%Y-%m-%d")
            if not first_error
            else False
        )

        if first_error or second_error:
            if first_error:
                messages.warning(request, "Fill all Date fields before Search!")
            else:
                messages.warning(
                    request,
                    "End Date must be greater than Start Date, Please try again.",
                )
            crypto_data = crypto_data_all
            df = pd.DataFrame.from_records(crypto_data.values())
            plot_crypto = plot_html(df, crypto_name)
            context["plot_crypto"] = plot_crypto
            return render(request, "app_crypto/plot.html", context)
        else:
            crypto_data = crypto_model.crypto_objects.between_dates(sd, ed)
            df = pd.DataFrame.from_records(crypto_data.values())
            print(crypto_data.values())
            plot_crypto = plot_html(df, crypto_name)
            context["plot_crypto"] = plot_crypto
            return render(request, "app_crypto/plot.html", context)
    else:
        crypto_data = crypto_data_all
        df = pd.DataFrame.from_records(crypto_data.values())
        plot_crypto = plot_html(df, crypto_name)
        context["plot_crypto"] = plot_crypto
        return render(request, "app_crypto/plot.html", context)


def update_database(request):
    crypto_models = getModels()
    crypto = []
    last_db_dates = []

    for i in crypto_models:
        crypto.append(i.__name__)
        last_db_dates.append(i.crypto_objects.last_date().date)

    data = dict(zip(crypto, last_db_dates))

    context = {
        "data": data,
    }

    return render(request, "app_crypto/update_database.html", context)
