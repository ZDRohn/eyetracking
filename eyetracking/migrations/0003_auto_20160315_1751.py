# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0002_gathereddata_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gathereddata',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]