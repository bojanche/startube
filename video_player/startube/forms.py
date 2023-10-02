from django import forms
from .models import Asset, Video
import datetime


class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video_name', )
        widgets = {'video_name': forms.TextInput(attrs={'id': 'video_name', 'class': 'form-control'}),}


class AddAssetFileForm(forms.Form):
    file = forms.FileField()
