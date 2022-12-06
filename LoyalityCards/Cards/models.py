from django.db import models
from django.utils import timezone


VISA = 'Visa'
MASTERCARD = 'MasterCard'
CHOICES = [
    (VISA, 4),
    (MASTERCARD, 5),
]

CHOICE_VD = ((12, 'Card for 12'), (6, 'Card for 6'), (1, 'Card for 12'))


class Card(models.Model):
    series = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=VISA,
    )
    card_number = models.CharField(max_length=16)
    card_released = models.DateTimeField(default=timezone.now)
    card_valid_date = models.IntegerField(choices=CHOICE_VD)

    card_use_date = models.DateTimeField(default=timezone.now)
    card_balance = models.IntegerField(default=0)
    card_status = models.BooleanField(default=False)
