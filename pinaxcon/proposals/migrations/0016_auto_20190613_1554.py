# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0015_auto_20190613_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencespeaker',
            name='website_url',
            field=models.URLField(blank=True, help_text='Personal website URL', verbose_name=b'Website URL'),
        ),
    ]
