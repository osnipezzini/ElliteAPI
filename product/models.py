from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField('Price', name='Price', max_digits=10, decimal_places=2)
    description = models.TextField('Description', null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name