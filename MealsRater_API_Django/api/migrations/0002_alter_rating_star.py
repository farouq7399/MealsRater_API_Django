# Generated by Django 3.2.5 on 2022-02-13 09:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxLengthValidator(5)]),
        ),
    ]
