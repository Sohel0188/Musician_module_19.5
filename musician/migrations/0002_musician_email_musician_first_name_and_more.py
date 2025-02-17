# Generated by Django 5.0.6 on 2024-06-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='musician',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='musician',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='musician',
            name='phone_number',
            field=models.CharField(default='', max_length=14),
        ),
    ]
