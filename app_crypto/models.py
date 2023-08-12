from django.db import models

# Create your models here.


class Ada(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Avax(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Bnb(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Btc(models.Model):
    date = models.TimeField(
        db_column="Date", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
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


class Busd(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Dai(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Doge(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Dot(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Etc(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Eth(models.Model):
    date = models.TextField(
        db_column="Date", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Hex(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Leo(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Ltc(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Matic(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Shib(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Sol(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Steth(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Trx(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Usdc(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Usdt(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Wbtc(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Wtrx(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.


class Xrp(models.Model):
    date = models.TextField(
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
    volume = models.IntegerField(
        db_column="Volume", blank=True, null=True
    )  # Field name made lowercase.
