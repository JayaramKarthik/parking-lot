# Generated by Django 3.2 on 2021-04-13 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lot_info', '0003_auto_20210413_1648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Slot',
            new_name='Row_Slot',
        ),
    ]