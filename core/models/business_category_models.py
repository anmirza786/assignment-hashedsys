from django.db import models
from core.status_enum import StatusEnum


class BusinessCategory(models.Model):
    category_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='Business Category Name')
    business_status = models.SmallIntegerField(
        default=1, choices=StatusEnum.choices, verbose_name='Business Status')
