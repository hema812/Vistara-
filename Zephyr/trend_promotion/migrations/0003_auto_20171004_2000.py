# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trend_promotion', '0002_auto_20171004_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='pnr',
            new_name='flightno',
        ),
    ]
