# Generated by Django 2.1.7 on 2019-03-06 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sheets', '0015_auto_20190306_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_sheets', to='exam_sheets.ExamSheet'),
        ),
    ]