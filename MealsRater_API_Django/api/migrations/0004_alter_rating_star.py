# Generated by Django 3.2.5 on 2022-02-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_rating_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.IntegerField(),
        ),
    ]
