# Generated by Django 4.2 on 2023-04-28 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myassess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='default_country', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default=True, max_length=15),
        ),
        migrations.AddField(
            model_name='customer',
            name='state_district',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='town',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=True, max_length=50),
        ),
    ]