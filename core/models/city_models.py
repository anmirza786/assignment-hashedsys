from django.db import models
from .country_models import Country


class City(models.Model):
    country = models.ForeignKey(
        Country, related_name='country', on_delete=models.CASCADE)
    city_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='City Name')

    def __str__(self):
        return str(self.country) + ', ' + str(self.city_name)
