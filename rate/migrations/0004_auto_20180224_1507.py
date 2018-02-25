# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_auto_20180224_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='message',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='微笑'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='ip_address',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='IP地址'),
        ),
    ]