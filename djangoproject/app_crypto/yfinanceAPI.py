import yfinance as yf
from datetime import date, timedelta, datetime

from django.apps import apps
from django.contrib import messages
from .models import *
import threading
import concurrent.futures

models_names = {
    "BTC",
    "ETH",
    "XRP",
    "ADA",
    "SOL",
    "DOGE",
    "DOT",
    "MATIC",
}

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
        date_to_be_updated = last_date_db + timedelta(days=1)
        ticker = assets[name.upper()]
        # messages.info(
        #     request, "Downloading data from Yahoo and Updating " + name + " database!"
        # )
        #### Getting a dataframe 5 day behind today to assure to get last date available! ####

        # messages.success(request, "Downloaded!")

        try:
            df = getCryptoByRangeData(ticker, date_to_be_updated, date.today())
            last_date_yahoo = sorted(list(df.Date), reverse=True)[0].date()

            if last_date_yahoo > last_date_db:
                populateTableByModel(df, i)
                messages.warning(
                    request,
                    "The Database "
                    + name
                    + " is out of date! Updated to: "
                    + str(last_date_yahoo),
                )

        except:
            messages.success(request, name.upper() + " is up to date!")


def home_table(assets):
    models = getModels()
    keys = range(7)
    titles = [
        "name",
        "lastPrice",
        "marketCap",
        "volume24h",
        "var_1h",
        "var_1d",
        "var_7d",
    ]

    def dataPerCrypto(cryptoModel):
        name = cryptoModel
        ticker = assets[name.upper()]
        yahoo_data = yf.Ticker(ticker)

        shortName = yahoo_data.info["shortName"]
        lastMomentAvailable = yahoo_data.history(interval="1m", period="1d").index[-1]
        oneHourAgo = lastMomentAvailable + timedelta(hours=-1)
        oneDayAgo = lastMomentAvailable + timedelta(days=-1)
        oneWeekAgo = lastMomentAvailable + timedelta(days=-7)
        mktCap = yahoo_data.info["marketCap"]
        vol24h = yahoo_data.info["volume24Hr"]

        def download_yf(moment):
            return yahoo_data.history(
                interval="1m", start=moment, end=moment + timedelta(minutes=1)
            )["Close"][0]

        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                t1 = executor.submit(download_yf, oneHourAgo)
                t2 = executor.submit(download_yf, oneDayAgo)
                t3 = executor.submit(download_yf, oneWeekAgo)
                t4 = executor.submit(download_yf, lastMomentAvailable)

                hourAgoData = t1.result()
                dayAgoData = t2.result()
                weekAgoData = t3.result()
                minuteAgoData = t4.result()

            var_1h = round(((minuteAgoData - hourAgoData) / hourAgoData) * 100, 2)
            var_1d = round(
                ((minuteAgoData - dayAgoData) / dayAgoData) * 100,
                2,
            )
            var_7d = round(
                ((minuteAgoData - weekAgoData) / weekAgoData) * 100,
                2,
            )

            values = [shortName, minuteAgoData, mktCap, vol24h, var_1h, var_1d, var_7d]
            data = {}

            for i in keys:
                data[titles[i]] = values[i]

            data["ticker"] = name.upper()

            return data

        except:
            values = ["*", "*", "*", "*", "*", "*", "*"]
            data = {}

            for i in keys:
                data[titles[i]] = values[i]

            data["ticker"] = name.upper()

            return data

    dicts = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(dataPerCrypto, i) for i in models_names]
        [dicts.append(f.result()) for f in futures]

    return dicts
