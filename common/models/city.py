# -*- coding: UTF-8 -*-
from django.db import models
from .state import State

class City(models.Model):
    name = models.CharField(max_length=256)
    state = models.ForeignKey(State, related_name='citys')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name