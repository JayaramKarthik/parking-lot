# Generated by Django 3.2 on 2021-04-13 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lot_info', '0002_auto_20210413_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column_Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='slot',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lot_info.column_slot'),
        ),
    ]
