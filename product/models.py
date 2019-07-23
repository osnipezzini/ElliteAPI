from django.db import models


# Create your models here.
from key.models import Key


class Product(models.Model):
    SERVER = 'SVR'
    CLIENT = 'CLI'
    MOBILE = 'MOB'
    WEB = 'WEB'
    PRODUCT_TYPE_CHOICES = [
        (SERVER, 'Server'),
        (CLIENT, 'Client'),
        (MOBILE, 'Mobile'),
        (WEB, 'Web'),
    ]

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField('Description', null=True, blank=True)
    slug = models.SlugField(null=True)
    limit_register = models.IntegerField(default=10)
    product_type = models.CharField(max_length=5, choices=PRODUCT_TYPE_CHOICES, default=CLIENT)
    keys = models.ManyToManyField(Key)

    def __str__(self):
        return self.name
