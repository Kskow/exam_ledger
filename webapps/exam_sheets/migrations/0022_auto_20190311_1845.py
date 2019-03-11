# Generated by Django 2.1.7 on 2019-03-11 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sheets', '0021_auto_20190310_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_sheet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='exam_sheets.ExamSheet'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
