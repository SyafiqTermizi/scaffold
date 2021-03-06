# Generated by Django 3.2.6 on 2021-08-14 02:15

from django.db import migrations, models
import django.utils.crypto
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_emailverificationtoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverificationtoken',
            name='token',
            field=models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(30,), **{}), max_length=255),
        ),
    ]
