# Generated by Django 3.1.1 on 2022-07-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
    ]
