# Generated by Django 5.0.1 on 2024-02-09 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_rename_author_music_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='username',
            new_name='email',
        ),
    ]
