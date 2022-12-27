from django.db import models
from core.status_enum import StatusEnum
from .category_models import Category


class SubCategory(models.Model):
    subcategory_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='Category Name')
    category_type = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE)
    subcategory_status = models.SmallIntegerField(
        default=1, choices=StatusEnum.choices, verbose_name='Category Status')
