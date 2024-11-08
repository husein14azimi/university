# Generated by Django 5.1.2 on 2024-11-02 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_coursestudentrelationship_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursestudentrelationship',
            name='semester',
            field=models.CharField(default=4031, max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_four_digit_number', message='Enter a 4-digit number', regex='^\\d{4}$')]),
            preserve_default=False,
        ),
    ]
