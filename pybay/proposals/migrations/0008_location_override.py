# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-16 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0007_ticket_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkproposal',
            name='location_override',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='location_override',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
