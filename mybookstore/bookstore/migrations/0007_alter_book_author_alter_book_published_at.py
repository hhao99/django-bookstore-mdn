# Generated by Django 4.2.7 on 2023-11-16 03:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_alter_book_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2023, 11, 16, 3, 33, 56, 132667, tzinfo=datetime.timezone.utc)),
        ),
    ]
