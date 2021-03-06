# Generated by Django 3.0.6 on 2020-08-14 17:46

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0038_auto_20200814_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gainlosshistory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 14, 23, 16, 17, 774263), null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 14, 23, 16, 17, 771608), null=True),
        ),
        migrations.AlterField(
            model_name='totalgainloss',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 14, 23, 16, 17, 773630), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 14, 23, 16, 17, 770641), null=True),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 14, 23, 16, 17, 773156), null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='identity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_identity_rel', to='accounts.IdentityDetails'),
        ),
        migrations.CreateModel(
            name='GainLossChartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gainloss_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 14, 23, 16, 17, 774849), null=True)),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_gl_chart_data_rel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
