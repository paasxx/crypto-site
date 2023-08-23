import yfinance as yf
from datetime import date, timedelta, datetime

from django.apps import apps
from django.contrib import messages
from .models import *


assets = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "USDT": "USDT-USD",
    "USDC": "USDC-USD",
    "BNB": "BNB-USD",
    "BUSD": "BUSD-USD",
    "XRP": "XRP-USD",
    "ADA": "ADA-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
    "DOT": "DOT-USD",
    "HEX": "HEX-USD",
    "SHIB": "SHIB-USD",
    "DAI": "DAI-USD",
    "WTRX": "WTRX-USD",
    "AVAX": "AVAX-USD",
    "MATIC": "MATIC-USD",
    "TRX": "TRX-USD",
    "STETH": "STETH-USD",
    "WBTC": "WBTC-USD",
    "LEO": "LEO-USD",
    "ETC": "ETC-USD",
    "LTC": "LTC-USD",
}


def getModelByName(modelName):
    model = apps.get_app_config("app_crypto").get_model(modelName)
    return model


def getModels():
    models = apps.get_app_config("app_crypto").get_models()
    return models


def getModelsNames():
    models = apps.get_app_config("app_crypto").get_models()
    models_names = []
    for i in models:
        models_names.append(i.__name__)
    return models_names


def getTablesNames():
    models = apps.get_app_config("app_crypto").get_models()
    models_names = []
    for i in models:
        models_names.append(i._meta.db_table)
    return models_names


## Example ticker="BTC-USD", startDate="2023-05-01", endDate="2023-12-03", date format YYYY-MM-DD
def getCryptoByRangeData(ticker, startDate, endDate):
    crypto_df = yf.download(ticker, startDate, endDate)
    df = crypto_df.reset_index(level=0)
    return df


def populateTableByModel(cryptoDataframe, cryptoModel):
    df = cryptoDataframe
    for i in df.index:
        vals = [df.at[i, col] for col in list(df.columns)]

        ##Change to use save function
        cryptoModel.crypto_objects.all_data().create(
            date=vals[0],
            # date=datetime.strftime(vals[0], "%Y-%m-%d"),
            open=vals[1],
            high=vals[2],
            low=vals[3],
            close=vals[4],
            adj_close=vals[5],
            volume=vals[6],
        )


def writeToDatabase(assets, request):
    models = getModels()

    for i in models:
        name = i.__name__
        ticker = assets[name.upper()]
        # messages.warning(request, "Downloading data from Yahoo and Updating Databases")
        df = getCryptoByRangeData(ticker, "2000-01-01", "2023-08-14")
        populateTableByModel(df, i)
        # messages.warning(request, "Done")


def updateDatabase(assets, request):
    models = getModels()

    for i in models:
        name = i.__name__
        last_date_db = i.crypto_objects.last_date().date
        ticker = assets[name.upper()]
        messages.info(
            request, "Downloading data from Yahoo and Updating " + name + " database!"
        )
        #### Getting a dataframe 5 day behind today to assure to get last date available! ####
        df = getCryptoByRangeData(
            ticker, date.today() + timedelta(days=-5), date.today()
        )
        last_date_yahoo = sorted(list(df.Date), reverse=True)[0].date()

        messages.success(request, "Downloaded!")

        if last_date_yahoo > last_date_db:
            populateTableByModel(df, i)
            messages.warning(
                request,
                "The Database "
                + name
                + " is out of date! Updated to: "
                + str(last_date_yahoo),
            )
        else:
            messages.success(
                request,
                "The Database "
                + name
                + " is up to date! Last date available: "
                + str(last_date_db),
            )
