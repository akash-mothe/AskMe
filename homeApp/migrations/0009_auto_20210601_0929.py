# Generated by Django 3.0.5 on 2021-06-01 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0008_auto_20210601_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersmodel',
            name='answer',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
    ]
