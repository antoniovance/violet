# -*- coding: UTF-8 -*-
from django.db import models
from common.models import CommonBase

class User(CommonBase):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_OTHER = 0
    GENDER_CHOICE = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
        (GENDER_OTHER, 'other')
    )
    username = models.CharField(max_length=256, null=False)
    password = models.CharField(max_length=256, null=False)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=GENDER_OTHER)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-created']