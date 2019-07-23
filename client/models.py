from django.db import models

# Create your models here.
from key.models import Key
from product.models import Product


class Company(models.Model):
    cnpj = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    server_ip = models.GenericIPAddressField()
    password = models.CharField(max_length=100, null=True, blank=True)
    product = models.ManyToManyField(Product, 'products')
    logo = models.ImageField('Company logo', 'company_logo', upload_to='img/', default='img/no-logo.png', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.password or self.password == '':
            password = ''.join(e for e in self.cnpj.__str__())
            from django.contrib.auth.hashers import make_password
            self.password = make_password(password[:8])
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
