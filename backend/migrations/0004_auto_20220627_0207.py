# Generated by Django 3.1.1 on 2022-06-27 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20220627_0203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-date_created']},
        ),
        migrations.RemoveField(
            model_name='room',
            name='date_updated',
        ),
        migrations.AlterField(
            model_name='room',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
