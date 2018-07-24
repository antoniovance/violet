# -*- coding: UTF-8 -*-
from django.db import models
from user.models import User

class ActivityTag(models.Model):
    name = models.CharField(max_length=128, default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    publisher = models.ForeignKey(User, related_name='activities')

    class Meta:
        pass  # todo： 继续完善发起者和参与者的关系
