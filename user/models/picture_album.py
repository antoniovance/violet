# -*- coding: UTF-8 -*-
from common.models import CommonBase
from django.db import models
from .user import User

class UserPictureAlbum(CommonBase):
    TYPE_HEADER = 1
    TYPE_OTHER = 2
    TYPE_CHOICE = (
        (TYPE_HEADER, 'header'),
        (TYPE_OTHER, 'other'),
    )
    name = models.CharField(max_length=256, default='')
    user = models.ForeignKey(User, related_name='albums')
    type = models.SmallIntegerField(choices=TYPE_CHOICE, default=TYPE_HEADER)

    class Meta:
        verbose_name = '像册'
        verbose_name_plural = verbose_name
        ordering = ['-created']


class UserPictureAlbumDetail(CommonBase):
    user = models.ForeignKey(User, related_name='album_details')
    album = models.ForeignKey(UserPictureAlbum, related_name='details')
    pic_url = models.CharField(max_length=256, default='')
    pic_file = models.ImageField()
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = '像册图片'
        verbose_name_plural = verbose_name
        ordering = ['-created']