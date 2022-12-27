from django.db import models
from .city_models import City
from .country_models import Country
from .category_models import Category
from .business_models import Business
from .subcategory_models import SubCategory


class Deal(models.Model):
    deal_sub_category = models.ForeignKey(
        SubCategory, related_name='deal_subcat', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    discount = models.PositiveIntegerField(
        null=False, blank=False, help_text='Max Discount 100%', verbose_name='Discount Percentages')
    description = models.TextField(blank=False, null=False)
