from django.db import models
from django.conf import settings
# Create your models here.

class PG(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    room_rent = models.IntegerField()
    mess_facility = models.BooleanField()
    gender = models.BooleanField()

    def __str__(self):
        return self.name
