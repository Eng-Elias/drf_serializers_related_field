from rest_framework import serializers

from duelists.models import DuelCard, Duelist


class DuelCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuelCard
        fields = '__all__'


class DuelCardField(serializers.RelatedField):

    def to_internal_value(self, data):
        try:
            duel_card_id = data
            return DuelCard.objects.get(id=duel_card_id)
        except ValueError:
            raise serializers.ValidationError(
                'Duel card id must be an integer.'
            )
        except DuelCard.DoesNotExist:
            raise serializers.ValidationError(
                'Duel card does not exist.'
            )

    def to_representation(self, value):
        return DuelCardSerializer(value, context=self.context).data


class DuelistSerializer(serializers.ModelSerializer):
    favourite_card = DuelCardField(queryset=DuelCard.objects.all())

    class Meta:
        model = Duelist
        fields = '__all__'
