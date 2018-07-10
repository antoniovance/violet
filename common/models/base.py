# -*- coding: UTF-8 -*-
from django.db import models


class CommonBase(models.Model):
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True