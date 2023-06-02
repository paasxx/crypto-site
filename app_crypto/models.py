from django.db import models

# Create your models here.


class Btc(models.Model):
    date = models.DateField(
        db_column="Date", blank=True, null=False, primary_key=True
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

    class Meta:
        managed = False
        db_table = "BTC"
