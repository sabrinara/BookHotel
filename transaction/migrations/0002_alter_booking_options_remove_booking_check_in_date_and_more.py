# Generated by Django 4.2.7 on 2024-02-05 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_out_date',
        ),
    ]
