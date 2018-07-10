# -*- coding: UTF-8 -*-
from common.models import CommonBase
from django.db import models

class email(CommonBase):
    email = models.EmailField(null=False)
