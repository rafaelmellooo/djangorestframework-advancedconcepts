from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    score = models.DecimalField(max_digits=3, decimal_places=2, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])

    class Meta:
        db_table = 'assessments'

    def __str__(self):
        return '%s - %s, %s' % (self.user.username, self.score, self.created_at)
