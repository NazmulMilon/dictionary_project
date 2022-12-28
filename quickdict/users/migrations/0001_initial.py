# Generated by Django 4.1.4 on 2022-12-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='users first name', max_length=100)),
                ('last_name', models.CharField(help_text='users last name', max_length=100)),
                ('user_name', models.CharField(help_text='users username', max_length=100)),
                ('email', models.EmailField(help_text='users personal email', max_length=100)),
                ('date_of_birth', models.DateField()),
                ('password_1', models.TextField(help_text='users password 1', max_length=15)),
                ('password_2', models.TextField(help_text="user's confirm password_2", max_length=15)),
            ],
        ),
    ]
