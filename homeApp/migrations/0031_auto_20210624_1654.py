# Generated by Django 3.0.5 on 2021-06-24 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homeApp', '0030_auto_20210624_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersmodel',
            name='ans_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answersmodel',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homeApp.QuestionsModel'),
        ),
    ]
