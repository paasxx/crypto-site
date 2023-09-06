from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .yfinanceAPI import *
from .plots import *
from .models import *
from django.http import JsonResponse


currencies = getTablesNames()
class_names = getModelsNames()


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username OR password is incorrect!")

        context = {}
        return render(request, "app_crypto/login.html", context)


@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("login")


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + user)
                return redirect("login")

        context = {"form": form}
        return render(request, "app_crypto/register.html", context)


@login_required(login_url="login")
def home(request):
    context = {
        "currencies": currencies,
        "class_names": class_names,
    }

    # writeToDatabase(assets, request)
    # print("Done")

    return render(request, "app_crypto/home.html", context)


@login_required(login_url="login")
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


@login_required(login_url="login")
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


@login_required(login_url="login")
def update_database(request):
    crypto_models = getModels()
    crypto = []
    last_db_dates = []
    first_db_dates = []

    for i in crypto_models:
        crypto.append(i.__name__)
        last_db_dates.append(i.crypto_objects.last_date().date)
        first_db_dates.append(i.crypto_objects.first_date().date)

    data = {}

    for i in range(len(crypto)):
        data[crypto[i]] = [first_db_dates[i], last_db_dates[i]]

    context = {
        "data": data,
    }

    return render(request, "app_crypto/update_database.html", context)


@login_required(login_url="login")
def update(request):
    updateDatabase(assets, request)
    return redirect("update_database")


@login_required(login_url="login")
def home_table_update(request):
    return JsonResponse(home_table(assets), safe=False)
