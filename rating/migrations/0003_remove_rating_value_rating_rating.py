# Generated by Django 5.0.1 on 2024-02-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_alter_rating_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='value',
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('01', '1'), ('02', '2'), ('03', '3'), ('04', '4'), ('05', '5'), ('06', '6'), ('07', '7'), ('08', '8'), ('09', '9'), ('10', '10')], default=0, max_length=2),
        ),
    ]