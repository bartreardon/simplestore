# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=200)),
                ('app_description', models.CharField(max_length=1000)),
                ('app_price', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200)),
                ('purchase_date', models.DateTimeField(verbose_name=b'date purchased')),
                ('purchased_app', models.ForeignKey(to='munkistore.Apps')),
            ],
        ),
    ]
