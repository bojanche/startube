from django.db import models
from datetime import datetime


# Create your models here.
class Asset(models.Model):
    asset_name = models.CharField(max_length=500)
    asset_type = models.CharField(max_length=20, blank=True)
    asset_upload_timestamp = models.DateTimeField(auto_now=True)
    asset_original = models.BooleanField(default=True)
    # asset_owner = models
    asset_dimension_x = models.IntegerField(null=True)
    asset_dimension_y = models.IntegerField(null=True)
    asset_duration = models.FloatField(null=True)
    asset_codec = models.CharField(max_length=20, blank=True)



class Video(models.Model):
    pass
    # asset = models.Fo
