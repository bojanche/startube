# Generated by Django 4.2.5 on 2023-09-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startube', '0003_video_asset_asset_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_file',
            field=models.FileField(default='c:\\', upload_to='%Y%m%d%H%M%S%f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='video_poster_location',
            field=models.CharField(default='c:\\', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_upload_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
