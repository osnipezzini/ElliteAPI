# Generated by Django 2.2.3 on 2019-07-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190723_1307'),
        ('client', '0006_auto_20190723_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='product',
        ),
        migrations.AddField(
            model_name='company',
            name='product',
            field=models.ManyToManyField(related_name='products', to='product.Product'),
        ),
    ]
