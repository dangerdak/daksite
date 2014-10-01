# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.TextField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default="I'm a Title", max_length=50),
            preserve_default=False,
        ),
    ]
