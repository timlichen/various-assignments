# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0003_auto_20161216_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='f_name',
        ),
    ]
