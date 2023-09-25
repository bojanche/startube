from django.db import models
from datetime import datetime


# Create your models here.
class Video(models.Model):
    video_name = models.CharField(max_length=500)
    # creator
    video_public = models.BooleanField(default=True)
    video_number_of_views = models.IntegerField(blank=True)
    video_poster_location = models.CharField(max_length=500)
    video_active = models.BooleanField(default=False)


class Asset(models.Model):
    asset_name = models.CharField(max_length=500)
    asset_type = models.CharField(max_length=20, blank=True)
    asset_upload_timestamp = models.DateTimeField(auto_now_add=True)
    asset_original = models.BooleanField(default=True)
    asset_file = models.FileField(upload_to='%Y%m%d%H%M%S%f')
    # asset_owner = models
    asset_dimension_x = models.IntegerField(null=True)
    asset_dimension_y = models.IntegerField(null=True)
    asset_duration = models.FloatField(null=True)
    asset_codec = models.CharField(max_length=20, blank=True)
    asset_video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True)



