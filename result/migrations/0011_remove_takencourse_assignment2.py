# pylint: disable-all
# Generated by Django 3.2.23 on 2024-03-07 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0010_alter_takencourse_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takencourse',
            name='assignment2',
        ),
    ]
