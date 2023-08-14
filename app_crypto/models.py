from django.db import models

# Create your models here.


class crypto(models.Model):
    date = models.DateField(
        db_column="Date", blank=True, null=True
    )  # Field name made lowercase.
    open = models.FloatField(
        db_column="Open", blank=True, null=True
    )  # Field name made lowercase.
    high = models.FloatField(
        db_column="High", blank=True, null=True
    )  # Field name made lowercase.
    low = models.FloatField(
        db_column="Low", blank=True, null=True
    )  # Field name made lowercase.
    close = models.FloatField(
        db_column="Close", blank=True, null=True
    )  # Field name made lowercase.
    adj_close = models.FloatField(
        db_column="Adj Close", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.BigIntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        abstract = True


class Ada(crypto):
    class Meta:
        db_table = "ADA"
        managed = True


class Avax(crypto):
    class Meta:
        db_table = "AVAX"
        managed = True


class Bnb(crypto):
    class Meta:
        db_table = "BNB"
        managed = True


class Btc(crypto):
    class Meta:
        db_table = "BTC"
        managed = True


class Busd(crypto):
    class Meta:
        db_table = "BUSD"
        managed = True


class Dai(crypto):
    class Meta:
        db_table = "DAI"
        managed = True


class Doge(crypto):
    class Meta:
        db_table = "DOGE"
        managed = True


class Dot(crypto):
    class Meta:
        db_table = "DOT"
        managed = True


class Etc(crypto):
    class Meta:
        db_table = "ETC"
        managed = True


class Eth(crypto):
    class Meta:
        db_table = "ETH"
        managed = True


class Hex(crypto):
    class Meta:
        db_table = "HEX"
        managed = True


class Leo(crypto):
    class Meta:
        db_table = "LEO"
        managed = True


class Ltc(crypto):
    class Meta:
        db_table = "LTC"
        managed = True


class Matic(crypto):
    class Meta:
        db_table = "MATIC"
        managed = True


class Shib(crypto):
    class Meta:
        db_table = "SHIB"
        managed = True


class Sol(crypto):
    class Meta:
        db_table = "SOL"
        managed = True


class Steth(crypto):
    class Meta:
        db_table = "STETH"
        managed = True


class Trx(crypto):
    class Meta:
        db_table = "TRX"
        managed = True


class Usdc(crypto):
    class Meta:
        db_table = "USDC"
        managed = True


class Usdt(crypto):
    class Meta:
        db_table = "USDT"
        managed = True


class Wbtc(crypto):
    class Meta:
        db_table = "WBTC"
        managed = True


class Wtrx(crypto):
    class Meta:
        db_table = "WTRX"
        managed = True


class Xrp(crypto):
    class Meta:
        db_table = "XRP"
        managed = True
