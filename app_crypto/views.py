from django.shortcuts import render
from datetime import datetime
from django.db.models import Max, Min
from django.contrib import messages
from .forms import *


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from plotly.offline import plot
from .yfinanceAPI import *


from .models import *
import sys
from django.apps import apps
from django.contrib import admin
from django.http import JsonResponse


currencies = getTablesNames()
class_names = getModelsNames()


def home(request):
    context = {
        "currencies": currencies,
        "class_names": class_names,
    }
    # writeToDatabase(assets, request)
    print(currencies)

    return render(request, "app_crypto/home.html", context)


def test(request):
    return render(request, "app_crypto/spinner.html")


def post_json(request):
    # instance = Ada.crypto_objects.all_data().order_by("date").values().first()
    crypto_model = getModelByName("Eth")
    instance = crypto_model.crypto_objects.between_dates(
        datetime(2023, 1, 1), datetime(2023, 1, 10)
    ).values()

    # print(instance)
    data = list(instance)
    return JsonResponse(data, safe=False)


def market(request, crypto):
    crypto_name = crypto
    crypto_model = getModelByName(crypto)

    sd = request.GET.get("startDate")
    ed = request.GET.get("endDate")

    min_date_table = crypto_model.crypto_objects.first_date().date
    max_date_table = crypto_model.crypto_objects.last_date().date

    crypto_data_all = crypto_model.crypto_objects.all_data()

    if sd == None and ed == None or sd == "" and ed == "":
        crypto_data = crypto_data_all

        context = {
            "currencies": currencies,
            "crypto": crypto_name,
            "crypto_data": crypto_data,
            "min_date_table": min_date_table,
            "max_date_table": max_date_table,
        }

        return render(request, "app_crypto/crypto_list.html", context)

    else:
        if datetime.strptime(ed, "%Y-%m-%d") < datetime.strptime(sd, "%Y-%m-%d"):
            messages.warning(
                request, "End Date must be greater than Start Date, Please try again."
            )
            crypto_data = crypto_data_all

            context = {
                "currencies": currencies,
                "crypto": crypto_name,
                "crypto_data": crypto_data,
                "min_date_table": min_date_table,
                "max_date_table": max_date_table,
            }

            return render(request, "app_crypto/crypto_list.html", context)

        else:
            if sd == None or sd == "":
                crypto_data = crypto_model.crypto_objects.lesser_or_equal_date(ed)

                context = {
                    "currencies": currencies,
                    "crypto": crypto_name,
                    "crypto_data": crypto_data,
                    "min_date_table": min_date_table,
                    "max_date_table": max_date_table,
                }

                return render(request, "app_crypto/crypto_list.html", context)

            elif ed == None or ed == "":
                crypto_data = crypto_model.crypto_objects.greater_or_equal_date(sd)

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
                crypto_data = crypto_model.crypto_objects.between_dates(
                    start_date, end_date
                )

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

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.07,
        subplot_titles=("OHLC", "Volume"),
        row_width=[0.2, 0.7],
    )

    # Plot OHLC on 1st row
    fig.add_trace(
        go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            showlegend=False,
        ),
        row=1,
        col=1,
    )

    fig.update_layout(
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        # plot_bgcolor="rgba(0, 0, 0, 0)",
        # paper_bgcolor="rgba(0, 0, 0, 0)",
    )

    fig.update_layout(
        title=title.upper(),
        yaxis_title="Price",
        autosize=True,
        # width=500,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=1),
    )

    fig.update_xaxes(
        mirror=True,
        ticks="outside",
        showline=True,
        # linecolor="grey",
        # gridcolor="grey",
        title_standoff=0,
        gridwidth=0.2,
        linewidth=0.1,
    )
    fig.update_yaxes(
        mirror=True,
        ticks="outside",
        showline=True,
        # linecolor="grey",
        # gridcolor="grey",
        title_standoff=10,
        gridwidth=0.2,
        linewidth=0.1,
    )

    def SetColor(df):
        color = []
        for i in df.index:
            if df["close"][i] > df["open"][i]:
                color.append("green")
            else:
                color.append("red")

        return color

    # Bar trace for volumes on 2nd row without legend
    fig.add_trace(
        go.Bar(
            x=df["date"],
            y=df["volume"],
            showlegend=False,
            marker=dict(color=SetColor(df)),
        ),
        row=2,
        col=1,
    )

    fig.update_layout(
        annotations=[
            go.layout.Annotation(
                {
                    "yshift": 10,
                    "font": dict(
                        # family="Courier New, monospace",
                        size=18,
                        # color="#ffffff"
                    ),
                }
            )
        ],
    )

    return fig.to_html()

    # fig.write_html(title + ".html")
    # fig.write_html(title + ".html")

    # fig.show()


def plot(request, crypto):
    crypto_name = crypto
    crypto_model = getModelByName(crypto)

    sd = request.GET.get("startDate")
    ed = request.GET.get("endDate")

    min_date_table = crypto_model.crypto_objects.first_date().date
    max_date_table = crypto_model.crypto_objects.last_date().date

    crypto_data_all = crypto_model.crypto_objects.all_data()

    if sd == None and ed == None or sd == "" and ed == "":
        crypto_data = crypto_data_all

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
        if datetime.strptime(ed, "%Y-%m-%d") < datetime.strptime(sd, "%Y-%m-%d"):
            messages.warning(
                request, "End Date must be greater than Start Date, Please try again."
            )
            crypto_data = crypto_data_all

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
            if sd == None or sd == "":
                crypto_data = crypto_model.crypto_objects.lesser_or_equal_date(ed)

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
                crypto_data = crypto_model.crypto_objects.greater_or_equal_date(sd)

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
                crypto_data = crypto_model.crypto_objects.between_dates(
                    start_date, end_date
                )

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
