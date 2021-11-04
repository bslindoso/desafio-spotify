# Generated by Django 3.2.3 on 2021-05-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210522_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spotify_Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=200, verbose_name='Client ID')),
                ('client_secret', models.CharField(max_length=200, verbose_name='Client Secret')),
            ],
        ),
    ]