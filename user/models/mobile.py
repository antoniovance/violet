# -*- coding: UTF-8 -*-
from common.models import CommonBase
from django.db import models
from .user import User

class mobile(CommonBase):
    mobile = models.CharField(max_length=128)
    user = models.ForeignKey(User, related_name='mobiles')

    class Meta:
        verbose_name = '手机号'
        verbose_name_plural = verbose_name
        ordering = ['-created']