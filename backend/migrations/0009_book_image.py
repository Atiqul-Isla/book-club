# Generated by Django 3.1.1 on 2022-07-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20220715_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, max_length=255, upload_to='images'),
            preserve_default=False,
        ),
    ]