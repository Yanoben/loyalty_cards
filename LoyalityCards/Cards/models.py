from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Card(models.Model):
    series = models.CharField(max_length=3)
    number = models.CharField(max_length=16)
    card_released = models.DateField()
    valid_date = models.DateField()
    status = models.BooleanField()
