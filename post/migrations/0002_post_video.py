# Generated by Django 5.0 on 2024-01-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]