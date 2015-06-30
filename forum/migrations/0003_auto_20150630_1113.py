# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
