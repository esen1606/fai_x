# Generated by Django 5.0 on 2024-01-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_rename_author_post_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]