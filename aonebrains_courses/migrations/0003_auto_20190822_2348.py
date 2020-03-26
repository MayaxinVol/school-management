# Generated by Django 2.2.3 on 2019-08-23 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('aonebrains_courses', '0002_auto_20190822_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(default=1, upload_to='videos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opencourse',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Grade'),
        ),
    ]