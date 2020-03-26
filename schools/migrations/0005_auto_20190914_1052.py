# Generated by Django 2.2.3 on 2019-09-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('schools', '0004_remove_school_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='schoolstudent',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, null=True, unique=True),
        ),
    ]