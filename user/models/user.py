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
    ORIENTATION_STRAIGHT = 1
    ORIENTATION_GAY = 2
    ORIENTATION_LESBIAN = 3
    ORIENTAIION_BISEXUAL = 4
    ORIENTAIION_TRANSGENDER = 5
    ORIENTAIION_OTHER = 6
    ORIENTATION_CHOICE = (
        (ORIENTATION_STRAIGHT, 'straight'),
        (ORIENTATION_GAY, 'gay'),
        (ORIENTATION_LESBIAN, 'lesbian'),
        (ORIENTAIION_BISEXUAL, 'bisexual'),
        (ORIENTAIION_TRANSGENDER, 'transgender'),
        (ORIENTAIION_OTHER, 'other')
    )
    username = models.CharField(max_length=256, null=False, db_index=True)
    password = models.CharField(max_length=256, null=False)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=GENDER_OTHER)
    orientation = models.SmallIntegerField(choices=ORIENTATION_CHOICE, default=None)
    birthday = models.DateField(null=True)
    introduce = models.TextField(default='')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-created']
        unique_together = (("username", ), )
