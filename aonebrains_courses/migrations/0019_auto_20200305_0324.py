# Generated by Django 2.2.3 on 2020-03-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aonebrains_courses', '0018_auto_20191023_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalopenmodule',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='openmodule',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
