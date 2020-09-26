# Generated by Django 3.0.6 on 2020-05-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200526_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='firm_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='person_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='person_relation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='identitydetails',
            name='citizenship',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='identitydetails',
            name='employment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='identitydetails',
            name='investment_experience',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='identitydetails',
            name='marital_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='identitydetails',
            name='ssn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
