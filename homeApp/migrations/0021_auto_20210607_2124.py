# Generated by Django 3.0.5 on 2021-06-07 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0020_followers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followers',
            old_name='followed_to',
            new_name='followed_by',
        ),
    ]
