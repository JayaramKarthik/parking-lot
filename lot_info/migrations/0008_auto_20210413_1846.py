# Generated by Django 3.2 on 2021-04-13 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lot_info', '0007_auto_20210413_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column_slot',
            old_name='column',
            new_name='column_name',
        ),
        migrations.RenameField(
            model_name='slot',
            old_name='row',
            new_name='row_name',
        ),
    ]
