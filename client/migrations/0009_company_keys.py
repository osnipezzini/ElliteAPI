# Generated by Django 2.2.3 on 2019-07-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0017_auto_20190723_2106'),
        ('client', '0008_remove_company_keys'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='keys',
            field=models.ManyToManyField(to='key.Key'),
        ),
    ]