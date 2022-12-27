from django.db import models
from .city_models import City
from .country_models import Country
from .business_category_models import BusinessCategory


class Business(models.Model):
    business_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='Business Name')
    country = models.ForeignKey(
        Country, related_name='business_country', on_delete=models.CASCADE)
    city = models.ForeignKey(
        City, related_name='business_city', on_delete=models.CASCADE)
    address = models.TextField(
        null=False, blank=False, verbose_name='Business Address')
    category = models.ForeignKey(
        BusinessCategory, related_name='business_city', on_delete=models.CASCADE)
    license_no = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='License Number')
    picture = models.FileField(upload_to='business/', null=True, blank=True)
