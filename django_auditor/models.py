# coding: utf-8

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from uuid import uuid1


class Auditor(models.Model):
    id = models.UUIDField(default=uuid1, primary_key=True)
    field = models.CharField(max_length=255, blank=True)
    action = models.CharField(max_length=6)
    old_value = models.TextField(blank=True, default='')
    new_value = models.TextField(blank=True, default='')
    stamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, blank=True, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField(blank=True)
    content_object = models.TextField()
    if 'tenant' in settings.AUDITOR:
        tenant = models.ForeignKey(settings.AUDITOR['tenant'],null=True,blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-stamp']
        db_table = 'auditor'
