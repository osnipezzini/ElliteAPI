# Generated by Django 2.2.3 on 2019-07-19 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20190605_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Company logo'),
        ),
    ]
