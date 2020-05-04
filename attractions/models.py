from django.db import models

from business_hours.models import BusinessHours


class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    business_days = models.ManyToManyField(BusinessHours)
    minimum_age = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'attractions'

    def __str__(self):
        return self.name
