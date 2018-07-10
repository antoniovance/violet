# -*- coding: UTF-8 -*-

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=256)

