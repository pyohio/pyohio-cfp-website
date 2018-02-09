# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinaxcon_registrasion', '0005_auto_20180208_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendeeprofile',
            name='agreement',
            field=models.BooleanField(default=False, help_text=b"I agree to act according to the <a href='/code-of-conduct'> PyOhio Code of Conduct</a>. I also agree with the PyOhio <a href='/terms'>Terms and Conditions</a>.", verbose_name=b'Agreement'),
        ),
        migrations.AlterField(
            model_name='attendeeprofile',
            name='newsletter',
            field=models.BooleanField(help_text=b'Select to be subscribed to the low-volume PyOhio announcements newsletter', verbose_name=b'Subscribe to PyOhio newsletter'),
        ),
    ]