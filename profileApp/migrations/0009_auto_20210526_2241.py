# Generated by Django 3.0.5 on 2021-05-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0008_auto_20210526_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_photo',
            field=models.ImageField(default='', upload_to='profile/images'),
            preserve_default=False,
        ),
    ]