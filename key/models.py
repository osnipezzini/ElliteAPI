import datetime

from django.db import models


# Create your models here.

class Key(models.Model):
    key = models.CharField(max_length=50)
    valid_date = models.DateField(default=datetime.datetime.today() + datetime.timedelta(days=30))

    def __str__(self):
        return self.key
