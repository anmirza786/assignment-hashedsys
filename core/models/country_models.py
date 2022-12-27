from django.db import models


class Country(models.Model):
    country_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='Country Name')
