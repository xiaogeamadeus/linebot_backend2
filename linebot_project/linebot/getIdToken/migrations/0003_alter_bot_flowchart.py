# Generated by Django 3.2.5 on 2022-07-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getIdToken', '0002_activation_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='flowChart',
            field=models.TextField(max_length=100),
        ),
    ]