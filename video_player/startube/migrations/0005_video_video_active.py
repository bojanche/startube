# Generated by Django 4.2.5 on 2023-09-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startube', '0004_asset_asset_file_video_video_poster_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_active',
            field=models.BooleanField(default=False),
        ),
    ]