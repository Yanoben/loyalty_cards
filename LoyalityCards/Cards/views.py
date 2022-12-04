from django.shortcuts import redirect, render, get_object_or_404
from .models import Card


def index(request):
    return render(request, 'home.html')


def generator_card():
    pass


def get_all_cards(request):
    cards = Card.objects.all()
    return render('page_cards.html', cards)


def get_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    context = {'card': card}
    return render('card.html', card_id=card_id, context=context)


def filter_card():
    pass


def change_status_card():
    pass


def delete_card(request, card_id):
    card = get_object_or_404(Card, card_id=card_id)
    card.delete()
    return render(request, 'page_cards.html')
