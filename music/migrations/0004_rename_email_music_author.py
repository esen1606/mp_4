# Generated by Django 5.0.1 on 2024-02-09 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_rename_username_music_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='email',
            new_name='author',
        ),
    ]
