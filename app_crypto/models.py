from django.db import models
from datetime import datetime
from django.db.models import Max, Min


# Create your models here.


class CryptoQuerySet(models.QuerySet):
    def all_data(self):
        return self.all()

    def last_date(self):
        return self.latest("date")

    def first_date(self):
        return self.earliest("date")

    def between_dates(self, startDate, endDate):
        return self.filter(date__gte=startDate, date__lte=endDate)

    def greater_or_equal_date(self, startDate):
        return self.filter(date__gte=startDate)

    def lesser_or_equal_date(self, endDate):
        return self.filter(date__gte=endDate)


class CryptoManager(models.Manager):
    def get_queryset(self):
        return CryptoQuerySet(self.model, using=self._db)

    def last_date(self):
        return self.get_queryset().last_date()

    def first_date(self):
        return self.get_queryset().first_date()

    def all_data(self):
        return self.get_queryset().all_data()

    def between_dates(self, startDate, endDate):
        return self.get_queryset().between_dates(startDate, endDate)

    def greater_or_equal_date(self, startDate):
        return self.get_queryset().greater_or_equal_date(startDate)

    def lesser_or_equal_date(self, endDate):
        return self.get_queryset().lesser_or_equal_date(endDate)


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

    crypto_objects = CryptoManager()


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
