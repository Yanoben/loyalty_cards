from django.forms import ModelForm
from .models import Card


class Gen_Card_Form(ModelForm):
    class Meta:
        model = Card
        fields = ['card_series', 'card_valid_date', 'card_count']
