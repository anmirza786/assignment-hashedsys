from django.db import models
from .city_models import City
from .country_models import Country
from .category_models import Category
from .business_models import Business
from .subcategory_models import SubCategory


class Deal(models.Model):
    cat = models.ForeignKey(
        Category, related_name='deal_cat', on_delete=models.SET_NULL, null=True)
    business = models.ForeignKey(
        Business, related_name='deal_business', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(
        City, related_name='deal_location', on_delete=models.SET_NULL, null=True)
    sub_cat = models.ForeignKey(
        SubCategory, related_name='deal_subcat', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    start = models.DateField(null=False, blank=False)
    end = models.DateField(null=False, blank=False)
    conditions = models.TextField()
    image = models.FileField(upload_to='deals', null=False, blank=False)
    discount = models.PositiveIntegerField(
        null=False, blank=False, help_text='Max Discount 100%', verbose_name='Discount Percentages')
    description = models.TextField(blank=False, null=False)
