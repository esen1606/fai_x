# Generated by Django 4.2.9 on 2024-01-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_rename_post_video_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.URLField(),
        ),
    ]
