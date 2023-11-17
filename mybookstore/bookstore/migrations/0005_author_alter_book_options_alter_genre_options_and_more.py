# Generated by Django 4.2.7 on 2023-11-16 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_book_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField(null=True)),
                ('date_of_death', models.DateField(null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-published_at']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2023, 11, 16, 1, 23, 27, 645898, tzinfo=datetime.timezone.utc)),
        ),
    ]
