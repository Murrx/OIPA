# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0002_auto_20141210_0542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='akvo_type',
            new_name='value_akvo_type',
        ),
        migrations.AddField(
            model_name='documentlink',
            name='title_akvo_type',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
