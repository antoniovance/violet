# -*- coding: UTF-8 -*-

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = '国家'
        verbose_name_plural = verbose_name
