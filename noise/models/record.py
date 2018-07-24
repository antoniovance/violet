# -*- coding: UTF-8 -*-
from common.models import CommonBase
from user.models import User
from django.db import models

class Record(CommonBase):
    title = models.CharField(max_length=128, default='')
    publisher = models.ForeignKey(User, related_name='records')
    record = models.FileField()


    class Meta:
        verbose_name = '音频记录'
        verbose_name_plural = verbose_name
        ordering = ['-created']