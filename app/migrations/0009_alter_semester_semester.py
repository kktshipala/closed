# pylint: disable-all
# Generated by Django 3.2.23 on 2024-03-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_semester_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.CharField(blank=True, choices=[('TERM 1', 'TERM 1'), ('TERM 2', 'TERM 2'), ('TERM 3', 'TERM 3'), ('TERM 4', 'TERM 4')], max_length=10),
        ),
    ]
