# -*- coding: UTF-8 -*-
from common.models import CommonBase
from django.db import models
from .user import User

class Email(CommonBase):
    email = models.EmailField(null=False)
    user = models.ForeignKey(User, related_name='emails')

    class Meta:
        verbose_name = '电子邮箱'
        verbose_name_plural = verbose_name
        ordering = ['-created']
