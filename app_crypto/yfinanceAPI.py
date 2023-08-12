import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import date, timedelta, datetime
import re
import requests
from .models import Btc


def BTC():
    crypto_df = yf.download("BTC-USD", start="2023-01-01", end="2023-01-10")
    df = crypto_df.reset_index(level=0)

    for i in df.index:
        print(df)
        vals = [df.at[i, col] for col in list(df.columns)]
        print(vals)
        print(type(vals[0]))
        print(vals[1])
        print(vals[2])
        print(vals[3])
        print(vals[4])
        print(vals[5])
        print(vals[6])

        Btc.objects.create(
            date=vals[0],
            open=vals[1],
            high=vals[2],
            low=vals[3],
            close=vals[4],
            adj_close=vals[5],
            volume=vals[6],
        )
