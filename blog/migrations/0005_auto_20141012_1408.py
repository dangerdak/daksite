# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20141001_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=blog.models.Image.get_path),
        ),
    ]
