# Generated by Django 5.0.1 on 2024-02-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_music_music_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music_text',
            field=models.TextField(default='text_music'),
        ),
    ]