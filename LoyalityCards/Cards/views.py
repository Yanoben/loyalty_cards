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
