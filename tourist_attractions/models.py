from django.db import models

from addresses.models import Address
from assessments.models import Assessment
from attractions.models import Attraction


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    is_approved = models.BooleanField(blank=True, default=False)
    attractions = models.ManyToManyField(Attraction)
    assessments = models.ManyToManyField(Assessment)
    address = models.OneToOneField(Address, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tourist_attractions'

    def __str__(self):
        return self.name
