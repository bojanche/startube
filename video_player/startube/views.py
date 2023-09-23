from django.shortcuts import render, redirect
from .models import Video, Asset

# Create your views here.


def home(request):
    video_list = Video.objects.all()
    return render(request, 'home.html', {'title': 'Home', 'video_list': video_list})


def video_admin(request):
    video_list = Video.objects.all()
    return render(request, 'video_admin.html', {'title': 'Video Admin', 'video_list': video_list})
