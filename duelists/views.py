from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from duelists.models import DuelCard, Duelist
from duelists.serializers import DuelCardSerializer, DuelistSerializer


class DuelCardListCreateAPIView(ListCreateAPIView):
    queryset = DuelCard.objects.all()
    serializer_class = DuelCardSerializer


class DuelCardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DuelCard.objects.all()
    serializer_class = DuelCardSerializer
    lookup_field = 'id'


class DuelistListCreateAPIView(ListCreateAPIView):
    queryset = Duelist.objects.all()
    serializer_class = DuelistSerializer


class DuelistRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Duelist.objects.all()
    serializer_class = DuelistSerializer
    lookup_field = 'id'
