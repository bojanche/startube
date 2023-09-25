from django.shortcuts import render, redirect
from .models import Video, Asset
from .forms import UploadFileForm

# Create your views here.


def home(request):
    video_list = Video.objects.all()
    return render(request, 'home.html', {'title': 'Home', 'video_list': video_list})


def video_admin(request):
    video_list = Video.objects.all()
    return render(request, 'video_admin.html', {'title': 'Video Admin', 'video_list': video_list})


def asset_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('startube:video_admin')
    else:
        form = UploadFileForm()
    return render(request, 'videoplayer/asset_upload.html', {'form':form})
