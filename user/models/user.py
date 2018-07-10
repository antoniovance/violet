# -*- coding: UTF-8 -*-
from django.db import models
from common.models import CommonBase

class User(CommonBase):
    GANDER_MALE = 1
    GANDER_FEMALE = 2
    GANDER_OTHER = 0
    GANDER_CHOICE = (
        (GANDER_MALE, 'male'),
        (GANDER_FEMALE, 'female'),
        (GANDER_OTHER, 'other')
    )
    username = models.CharField(max_length=256, null=False)
    password = models.CharField(max_length=256, null=False)
    gander = models.SmallIntegerField(choices=GANDER_CHOICE, default=GANDER_OTHER)
