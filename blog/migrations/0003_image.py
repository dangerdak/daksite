# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140928_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
