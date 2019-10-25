from django.db import models
from django.conf import settings
# Create your models here.

class PG(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    room_rent = models.IntegerField()
    mess_facility = models.BooleanField()
    gender_choices = [
        ('B', 'Boy'),
        ('G', 'Girl'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=gender_choices,
        default='B',
    )
    dist_from_cllg = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.name
