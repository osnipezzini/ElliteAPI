from django.db import models

# Create your models here.
from api import settings
from key.models import Key
from product.models import Product


class Company(models.Model):
    cnpj = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    server_ip = models.GenericIPAddressField()
    password = models.CharField(max_length=100)
    keys = models.ManyToManyField(Key, 'keys', 'company_key')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
    logo = models.ImageField('Company logo', 'company_logo', upload_to='img/', default='img/no-logo.png')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.password:
            password = ''.join(e for e in self.cnpj.__str__())
            self.password = password[:8]
        super(Company, self).save(*args, **kwargs)

    def get_logo_url(self):
        print(self.company_logo.url)
        if self.company_logo:
            logo = "{0}".format(self.company_logo.url)
            print(logo)
            return logo
        else:
            return ''


class Client(models.Model):
    cpf = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
