# Generated by Django 3.1.4 on 2020-12-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
