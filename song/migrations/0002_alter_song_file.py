# Generated by Django 4.0.5 on 2023-04-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(upload_to='files/songs/'),
        ),
    ]
