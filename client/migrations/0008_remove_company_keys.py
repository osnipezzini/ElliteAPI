# Generated by Django 2.2.3 on 2019-07-23 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20190723_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='keys',
        ),
    ]
