import yfinance as yf
from datetime import date, timedelta, datetime

from django.apps import apps
from django.contrib import messages


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
        cryptoModel.objects.create(
            date=datetime.strftime(vals[0], "%Y-%m-%d"),
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
