# Generated by Django 5.0.1 on 2024-02-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customuser_is_author_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_author',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
