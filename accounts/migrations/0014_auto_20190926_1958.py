# Generated by Django 2.2.3 on 2019-09-27 02:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0013_auto_20190923_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='phone',
            field=models.IntegerField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(max_length=12, null=True),
        ),
    ]