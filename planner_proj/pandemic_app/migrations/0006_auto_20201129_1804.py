# Generated by Django 3.1.2 on 2020-11-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic_app', '0005_auto_20201129_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.AddField(
            model_name='class',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lecture',
            name='day',
            field=models.DateField(),
        ),
    ]
