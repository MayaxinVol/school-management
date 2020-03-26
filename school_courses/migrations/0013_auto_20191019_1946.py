# Generated by Django 2.2.3 on 2019-10-20 02:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('school_courses', '0012_auto_20191013_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolcontent',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('stext', 'svideo', 'simage', 'sfile')}, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='schoolcontent',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contents',
                                    to='school_courses.SchoolModule'),
        ),
        migrations.AlterField(
            model_name='schoolcourse',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='courses_created', to='schools.Teacher'),
        ),
        migrations.AlterField(
            model_name='schoolcourse',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='grade', to='accounts.Grade'),
        ),
        migrations.AlterField(
            model_name='schoolcourse',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses',
                                    to='schools.School'),
        ),
        migrations.AlterField(
            model_name='schoolcourse',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses',
                                    to='school_courses.SchoolSubject'),
        ),
        migrations.AlterField(
            model_name='schoolmodule',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modules',
                                    to='school_courses.SchoolCourse'),
        ),
        migrations.AlterField(
            model_name='schoolsubject',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects',
                                    to='schools.School'),
        ),
        migrations.AlterField(
            model_name='sfile',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='sfile_related', to='schools.Teacher'),
        ),
        migrations.AlterField(
            model_name='simage',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='simage_related', to='schools.Teacher'),
        ),
        migrations.AlterField(
            model_name='stext',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='stext_related', to='schools.Teacher'),
        ),
        migrations.AlterField(
            model_name='svideo',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='svideo_related', to='schools.Teacher'),
        ),
    ]