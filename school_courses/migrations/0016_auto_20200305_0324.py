# Generated by Django 2.2.3 on 2020-03-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_courses', '0015_auto_20191023_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalschoolmodule',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='schoolmodule',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]