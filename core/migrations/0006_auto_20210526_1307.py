# Generated by Django 3.2.3 on 2021-05-26 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210526_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='links',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='musicas',
        ),
    ]