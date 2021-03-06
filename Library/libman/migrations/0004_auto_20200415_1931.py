# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-04-15 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libman', '0003_auto_20180526_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='barcode',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.CharField(choices=[(b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020')], max_length=4),
        ),
    ]
