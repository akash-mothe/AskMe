# Generated by Django 3.0.5 on 2021-05-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('dis_name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
