# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='password',
            new_name='password1',
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
