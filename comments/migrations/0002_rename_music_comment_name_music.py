# Generated by Django 5.0.1 on 2024-02-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='music',
            new_name='name_music',
        ),
    ]
