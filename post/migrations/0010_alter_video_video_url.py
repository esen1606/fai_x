# Generated by Django 4.2.9 on 2024-01-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_video_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.CharField(max_length=250),
        ),
    ]