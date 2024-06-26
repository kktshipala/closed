# pylint: disable-all
# Generated by Django 3.2.23 on 2024-01-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_alter_result_id_alter_takencourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='assignment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 18/01/24', ' 18/01/24'), ('* 18/01/24', '* 18/01/24')], max_length=200),
        ),
    ]
