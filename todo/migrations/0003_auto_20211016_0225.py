# Generated by Django 3.2.8 on 2021-10-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_board_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='compeleted',
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
