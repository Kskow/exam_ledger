# Generated by Django 2.1.7 on 2019-03-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sheets', '0012_auto_20190304_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examsheet',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='examsheet',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]