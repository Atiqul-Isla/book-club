# Generated by Django 3.1.1 on 2022-07-19 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20220715_2306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-date_created']},
        ),
    ]
