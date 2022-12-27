from django.db import models
from core.status_enum import StatusEnum


class Category(models.Model):
    category_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='Category Name')
    category_status = models.SmallIntegerField(
        default=1, choices=StatusEnum.choices, verbose_name='Category Status')

    def __str__(self):
        return str(self.category_name)
