# Generated by Django 3.1.4 on 2020-12-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0005_auto_20201221_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
