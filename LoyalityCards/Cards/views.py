from django.shortcuts import redirect, render, get_object_or_404
from .models import Card
from .forms import Gen_Card_Form, Get_Cards
from random import randint


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def get_all_cards(request):
    cards = Card.objects.all()
    form = Get_Cards()
    context = {'cards': cards,
               'form': form}
    return render(request, 'page_cards.html', context)


def generator_card(request):
    form = Gen_Card_Form()
    context = {'form': form}
    number = random_with_N_digits(15)
    if request.method == 'POST':
        count = request.POST.get('count')
        card_valid_date = request.POST.get('card_valid_date')
        series = request.POST.get('series')
        if series == 'Visa':
            number = '4' + str(number)
        else:
            number = '5' + str(number)
        for _ in range(int(count)):
            card = Card(
                series=series,
                card_number=number,
                card_valid_date=card_valid_date)
            card.save()
        return redirect('get_all_cards')
    return render(request, 'gen_card.html', context)


def get_card(request, card_id):
    form = Get_Cards()
    card = get_object_or_404(Card, pk=card_id)
    context = {'card': card,
               'form': form}
    return render(request, 'card.html', context=context)


def filter_card():
    # todo
    pass


def change_status_card(request, card_id):
    form = Get_Cards()
    card = get_object_or_404(Card, pk=card_id)
    context = {'card': card,
               'form': form}
    if card.card_status:
        card = Card.objects.filter(pk=card_id).update(card_status=False)
        return render(request, 'card.html', context=context)
    else:
        card = Card.objects.filter(pk=card_id).update(card_status=True)
        return render(request, 'card.html', context=context)


def delete_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    card.delete()
    return redirect(request, 'page_cards.html')
