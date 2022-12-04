from django.urls import path
from views import (home, get_all_cards, get_card, filter_card,
                   change_status_card, delete_card)


urlpatterns = [
    path('', home, 'home'),
    path('get_all/', get_all_cards, name='get_all_cards'),
    path('<int:card_id>/', get_card, name='get_card'),
    path('filter/', filter_card, name='filter'),
    path('change-status/', change_status_card, 'change_status'),
    path('<int:card_id>/delete/', delete_card, "delete_card"),
]
