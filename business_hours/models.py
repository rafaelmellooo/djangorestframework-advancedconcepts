from django.db import models


class BusinessHours(models.Model):
    class Weekday(models.IntegerChoices):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

        def __str__(self):
            return self.value

    weekday = models.IntegerField(choices=Weekday.choices)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        verbose_name_plural = 'Business Hours'
        db_table = 'business_hours'

    def __str__(self):
        return '%s, %s - %s' % (self.Weekday.choices[self.weekday - 1][1],
                                self.opening_time,
                                self.closing_time)
