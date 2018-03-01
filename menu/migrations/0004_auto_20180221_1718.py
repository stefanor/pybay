# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-22 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20180221_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='target',
            field=models.BooleanField(default=False, help_text='Check to open in new window'),
        ),
        migrations.AlterField(
            model_name='submenuitem',
            name='target',
            field=models.BooleanField(default=False, help_text='Check to open in new window'),
        ),
    ]