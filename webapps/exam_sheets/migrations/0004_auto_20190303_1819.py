# Generated by Django 2.1.7 on 2019-03-03 18:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sheets', '0003_auto_20190303_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='assigned_points',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
