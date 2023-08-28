from django.db import models


class CryptoQuerySet(models.QuerySet):
    def all_data(self):
        return self.all()

    def last_date(self):
        return self.latest("date")

    def first_date(self):
        return self.earliest("date")

    def between_dates(self, startDate, endDate):
        return self.filter(date__gte=startDate, date__lte=endDate)

    ## Throw some errors messages

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
