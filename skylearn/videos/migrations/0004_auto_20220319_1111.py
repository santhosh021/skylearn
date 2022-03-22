# Generated by Django 3.2.5 on 2022-03-19 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='id',
        ),
        migrations.AddField(
            model_name='videos',
            name='video_name_slug',
            field=models.SlugField(default='', max_length=256, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name_slug',
            field=models.SlugField(max_length=256, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video_name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
