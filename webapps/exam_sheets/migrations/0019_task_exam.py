# Generated by Django 2.1.7 on 2019-03-10 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sheets', '0018_auto_20190309_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam_sheets.Exam'),
        ),
    ]