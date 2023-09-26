from django import forms
from .models import Asset, Video


class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video_name', 'video_public', 'video_active')