# -*- coding: UTF-8 -*-
from common.models import CommonBase
from django.db import models

class mobile(CommonBase):
    mobile = models.CharField(max_length=128)