# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbxapp', '0003_auto_20180430_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
