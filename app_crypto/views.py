from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.db.models import Max, Min

import pandas as pd

# import yfinance as yf
# from yahoofinancials import YahooFinancials
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from plotly.offline import plot


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

    min_date_table_str = crypto.objects.aggregate(Min("date"))["date__min"]
    max_date_table_str = crypto.objects.aggregate(Max("date"))["date__max"]

    min_date_table = datetime.strptime(min_date_table_str, "%Y-%m-%d %H:%M:%S")
    max_date_table = datetime.strptime(max_date_table_str, "%Y-%m-%d %H:%M:%S")

    if sd == None and ed == None or sd == "" and ed == "":
        crypto_data = crypto.objects.all()
        print(type(crypto_data))

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
        }

        return render(request, "app_crypto/crypto_list.html", context)

    elif sd == None or sd == "":
        crypto_data = crypto.objects.filter(date__lte=ed)

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
        }

        return render(request, "app_crypto/crypto_list.html", context)

    elif ed == None or ed == "":
        crypto_data = crypto.objects.filter(date__gte=sd)

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


def plot_html(df, title):
    # df = df_from_sql_query(crypto, "Date", conn, startDate, endDate)

    df["date"] = pd.to_datetime(df["date"])

    df = df.drop(columns=["adj_close"])

    #     eth_df.set_index('Date')

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["date"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"],
            )
        ]
    )

    fig.update_layout(xaxis_rangeslider_visible=False)

    fig.update_layout(
        title=title,
        yaxis_title="Price",
    )
    print(type(fig))
    # figu = plot({"data": fig}, output_type="div")
    return fig.to_html()

    # fig.write_html(title + ".html")
    # fig.write_html(title + ".html")

    # fig.show()


def plot(request, crypto):
    crypto_name = crypto
    crypto = getattr(sys.modules[__name__], crypto)

    sd = request.GET.get("startDate")
    ed = request.GET.get("endDate")

    min_date_table_str = crypto.objects.aggregate(Min("date"))["date__min"]
    max_date_table_str = crypto.objects.aggregate(Max("date"))["date__max"]

    min_date_table = datetime.strptime(min_date_table_str, "%Y-%m-%d %H:%M:%S")
    max_date_table = datetime.strptime(max_date_table_str, "%Y-%m-%d %H:%M:%S")

    if sd == None and ed == None or sd == "" and ed == "":
        crypto_data = crypto.objects.all()
        df = pd.DataFrame.from_records(crypto_data.values())

        plot_crypto = plot_html(df, crypto_name)

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
            "plot_crypto": plot_crypto,
        }

        return render(request, "app_crypto/plot.html", context)

    elif sd == None or sd == "":
        crypto_data = crypto.objects.filter(date__lte=ed)
        df = pd.DataFrame.from_records(crypto_data.values())

        plot_crypto = plot_html(df, crypto_name)

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
            "plot_crypto": plot_crypto,
        }

        return render(request, "app_crypto/plot.html", context)

    elif ed == None or ed == "":
        crypto_data = crypto.objects.filter(date__gte=sd)
        df = pd.DataFrame.from_records(crypto_data.values())

        plot_crypto = plot_html(df, crypto_name)

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
            "plot_crypto": plot_crypto,
        }

        return render(request, "app_crypto/plot.html", context)

    else:
        start_date = datetime.strptime(sd, "%Y-%m-%d")
        end_date = datetime.strptime(ed, "%Y-%m-%d")
        crypto_data = crypto.objects.filter(
            date__range=[start_date, end_date]
        ).distinct()
        df = pd.DataFrame.from_records(crypto_data.values())

        plot_crypto = plot_html(df, crypto_name)

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
            "plot_crypto": plot_crypto,
        }

        return render(request, "app_crypto/plot.html", context)
