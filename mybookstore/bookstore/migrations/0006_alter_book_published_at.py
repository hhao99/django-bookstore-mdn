# Generated by Django 4.2.7 on 2023-11-16 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_author_alter_book_options_alter_genre_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2023, 11, 16, 3, 29, 20, 815578, tzinfo=datetime.timezone.utc)),
        ),
    ]