# -*- coding: UTF-8 -*-

from common.models import CommonBase
from django.db import models
from user.models import User
from .record import Record

class RecordComment(CommonBase):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    record = models.ForeignKey(Record, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(default='')
    stars = models.DurationField()

    class Meta:
        verbose_name = '音频记录评论'
        verbose_name_plural = verbose_name
        ordering = ['-created']