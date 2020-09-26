# Generated by Django 3.0.6 on 2020-06-14 15:37

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200614_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='history_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 14, 21, 7, 21, 962122), null=True),
        ),
    ]
