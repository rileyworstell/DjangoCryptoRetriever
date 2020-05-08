from django.db import models

class TopCurrencies(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=50)