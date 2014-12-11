# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0003_auto_20141211_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='aidstream_id',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
