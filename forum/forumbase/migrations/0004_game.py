# Generated by Django 4.0.6 on 2022-08-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumbase', '0003_question_likes_alter_question_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('studio', models.CharField(max_length=64)),
            ],
        ),
    ]
