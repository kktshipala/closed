# Generated by Django 3.2.23 on 2024-04-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0031_alter_takencourse_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 24/04/24', ' 24/04/24'), ('* 24/04/24', '* 24/04/24')], max_length=200),
        ),
    ]
