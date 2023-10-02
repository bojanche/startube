from django.shortcuts import render, redirect
from .models import Video, Asset
from .forms import CreateVideoForm, AddAssetFileForm
from .utilities import *
from django.core.files.storage import FileSystemStorage
from video_player.settings import MEDIA_ROOT
# Create your views here.


def home(request):
    video_list = Video.objects.all()
    return render(request, 'home.html', {'title': 'Home', 'video_list': video_list})


def video_admin(request):
    video_list = Video.objects.all()
    if request.method == 'GET':
        form = CreateVideoForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('startube:video_admin')
    else:
        form = CreateVideoForm()
    return render(request, 'video_admin.html', {'title': 'Video Admin', 'video_list': video_list, 'form': form})


def video_properties(request, id):
    video = Video.objects.get(id=id)
    assets = Asset.objects.filter(asset_video=id)
    if request.method == 'POST':
        form = AddAssetFileForm(request.POST, request.FILES)
        if form.is_valid():
            loc = MEDIA_ROOT / video.video_name
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage(location=loc)
            filename = fs.save(uploaded_file.name, uploaded_file)
            asset = Asset(asset_name=uploaded_file.name, asset_video=video)
            asset.save()
            return redirect('startube:video_properties', id=id)
    else:
        form = AddAssetFileForm()
    return render(request, 'video_properties.html', {'title': 'Uređivanje', 'video': video, 'assets': assets, 'form': form})

