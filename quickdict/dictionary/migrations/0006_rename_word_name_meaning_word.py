# Generated by Django 4.1.4 on 2022-12-29 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0005_alter_meaning_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meaning',
            old_name='word_name',
            new_name='word',
        ),
    ]
