# -*- coding: UTF-8 -*-
from django.db import models

class TagBase(models.Model):

    class Meta:
        abstract = True