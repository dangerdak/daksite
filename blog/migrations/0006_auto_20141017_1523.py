# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20141012_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
