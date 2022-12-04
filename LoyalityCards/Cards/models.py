from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Card(models.Model):
    card_series = models.CharField(max_length=3)
    card_number = models.CharField(max_length=16)
    card_released = models.DateTimeField("date released", auto_now_add=True)
    card_valid_date = models.DateTimeField()
    card_use_date = models.DateTimeField()
    card_balance = models.IntegerField()
    card_status = models.BooleanField()
