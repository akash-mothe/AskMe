# Generated by Django 3.0.5 on 2021-06-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0024_auto_20210607_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='followed_by',
            field=models.IntegerField(),
        ),
    ]