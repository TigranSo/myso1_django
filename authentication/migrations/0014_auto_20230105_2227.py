# Generated by Django 3.2.16 on 2023-01-05 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_profile_domofon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='comet',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='domofon',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='etaj',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='kvartir',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='podezd',
        ),
    ]
