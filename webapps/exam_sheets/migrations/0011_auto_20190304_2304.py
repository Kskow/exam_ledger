# Generated by Django 2.1.7 on 2019-03-04 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sheets', '0010_auto_20190304_2252'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('task', 'user')},
        ),
    ]