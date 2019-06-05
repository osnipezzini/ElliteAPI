from django.contrib import admin

# Register your models here.
from client.models import Company, Client

admin.site.register(Client)
admin.site.register(Company)
