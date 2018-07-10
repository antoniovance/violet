# -*- coding: UTF-8 -*-

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = '公司'
        verbose_name_plural = verbose_name
