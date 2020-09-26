# Generated by Django 3.0.6 on 2020-06-14 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200614_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockhistory',
            name='last_update',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 14, 23, 26, 12, 75813), null=True),
        ),
    ]