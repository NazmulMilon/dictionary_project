# Generated by Django 4.1.4 on 2022-12-29 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_alter_meaning_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='meaning',
            table='meanings',
        ),
    ]
