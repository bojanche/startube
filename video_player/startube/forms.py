from django import forms
from .models import Asset, Video
import datetime


class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video_name', 'video_container_location')
        widgets = {'video_name': forms.TextInput(attrs={'id': 'video_name', 'class': 'form-control'}),
                   'video_container_location': forms.HiddenInput(attrs={'id': 'folder', 'name': 'video_location',
                                                                        'value': datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'),
                                                                        'placeholder': ''})}


class AddAssetFileForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('asset_file', 'asset_video')