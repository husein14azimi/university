# Generated by Django 5.1.2 on 2024-11-02 06:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('minimum_grade_to_pass', models.FloatField(help_text='the range for this field is from 0 to 20', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(20.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CourseStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudentRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(blank=True, help_text='the range for this field is from 0 to 20', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(20.0)])),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='course.course')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.student')),
            ],
        ),
    ]
