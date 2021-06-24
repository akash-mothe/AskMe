# Generated by Django 3.0.5 on 2021-06-24 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homeApp', '0029_remove_questionsmodel_got_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersmodel',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people_answers', to='homeApp.QuestionsModel'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
