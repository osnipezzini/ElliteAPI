# Generated by Django 2.2.3 on 2019-07-23 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0011_auto_20190723_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='valid_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 22, 12, 56, 22, 550160)),
        ),
    ]
