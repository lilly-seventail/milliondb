# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_remove_idol_og_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='idol',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
