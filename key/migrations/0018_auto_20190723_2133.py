# Generated by Django 2.2.3 on 2019-07-24 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0017_auto_20190723_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='valid_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 22, 21, 33, 12, 847153)),
        ),
    ]
