# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0002_auto_20161215_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='alias',
        ),
    ]
