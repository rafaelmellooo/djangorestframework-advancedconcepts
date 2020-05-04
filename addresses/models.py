from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=40, null=True)
    uf = models.CharField(max_length=2)
    city = models.CharField(max_length=80)
    neighborhood = models.CharField(max_length=80)
    street = models.CharField(max_length=80)
    number = models.PositiveIntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'addresses'
        db_table = 'addresses'

    def __str__(self):
        return '%s, %s - %s, %s - %s, %s' % (self.country, self.uf, self.city,
                                             self.neighborhood, self.street,
                                             self.number)
