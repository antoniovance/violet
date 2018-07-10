# -*- coding: UTF-8 -*-

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=256)
