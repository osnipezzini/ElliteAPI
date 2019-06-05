from django.db import models

# Create your models here.
from key.models import Key
from product.models import Product


class Company(models.Model):
    cnpj = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    server_ip = models.GenericIPAddressField()
    password = models.CharField(max_length=100)
    key = models.ForeignKey(Key, on_delete=models.DO_NOTHING, null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    cpf = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
