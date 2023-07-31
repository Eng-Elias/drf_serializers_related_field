from django.urls import path

from duelists import views


urlpatterns = [
    path('duel_cards/', views.DuelCardListCreateAPIView.as_view(), name='duel_card_list_create'),
    path('duel_card/<int:id>', views.DuelCardRetrieveUpdateDestroyAPIView.as_view(), name='duel_card_retrieve_update_destroy'),
    path('duelists', views.DuelistListCreateAPIView.as_view(), name='duelist_list_create'),
    path('duelist/<int:id>', views.DuelistRetrieveUpdateDestroyAPIView.as_view(), name='duelist_retrieve_update_destroy'),
]
