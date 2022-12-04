from django.shortcuts import redirect, render, get_object_or_404
from .models import Card
from .forms import Gen_Card_Form, Get_Cards


def generator_card(request):
    form = Gen_Card_Form()
    if request.method == 'GET':
        form = Gen_Card_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form': form}
        return render(request, 'gen_card.html', context)
    else:
        return redirect('')


def get_all_cards(request):
    cards = Card.objects.all()
    form = Get_Cards()
    context = {'cards': cards,
               'form': form}
    return render(request, 'page_cards.html', context)


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
