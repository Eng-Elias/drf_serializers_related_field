from django.db import models


class DuelCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    type = models.CharField(choices=[('monster', 'Monster'), ('spell', 'Spell'), ('trap', 'Trap')], max_length=20)


class Duelist(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    favourite_card = models.ForeignKey(DuelCard, on_delete=models.SET_NULL, blank=True, null=True)
