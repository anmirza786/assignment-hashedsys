from django.db import models


class StatusEnum(models.IntegerChoices):
    ACTIVE = 1, 'Active'
    INACTIVE = 2, 'Inactive'
