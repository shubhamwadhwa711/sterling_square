# Generated by Django 3.0.6 on 2020-05-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
