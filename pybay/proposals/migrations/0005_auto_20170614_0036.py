# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-14 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0004_auto_20170516_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkproposal',
            name='speaker_website',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='speaker_website',
            field=models.TextField(null=True),
        ),
    ]