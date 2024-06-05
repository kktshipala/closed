# pylint: disable-all
# Generated by Django 3.2.23 on 2024-03-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_course_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('First', 'First'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth')], max_length=200),
        ),
    ]