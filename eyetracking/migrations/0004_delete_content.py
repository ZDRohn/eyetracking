# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-12 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0003_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Content',
        ),
    ]
