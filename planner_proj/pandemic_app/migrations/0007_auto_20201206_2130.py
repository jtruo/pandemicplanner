# Generated by Django 3.1.3 on 2020-12-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic_app', '0006_auto_20201129_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(),
        ),
    ]