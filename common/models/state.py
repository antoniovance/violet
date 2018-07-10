# -*- coding: UTF-8 -*-
from django.db import models
from .country import Country

class State(models.Model):
    name = models.CharField(max_length=256)
    country = models.ForeignKey(Country, related_name='states')

    class Meta:
        verbose_name = '省/州'
        verbose_name_plural = verbose_name