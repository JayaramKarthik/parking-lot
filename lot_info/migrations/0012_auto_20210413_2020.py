# Generated by Django 3.2 on 2021-04-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot_info', '0011_auto_20210413_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='is_filled',
        ),
        migrations.AddField(
            model_name='column_slot',
            name='is_filled',
            field=models.BooleanField(default=False),
        ),
    ]
