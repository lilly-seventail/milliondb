# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20170731_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]