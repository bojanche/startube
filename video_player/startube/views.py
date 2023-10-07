from django.shortcuts import render, redirect
from .models import Video, Asset
from .forms import CreateVideoForm, AddAssetFileForm
from .utilities import *
from django.core.files.storage import FileSystemStorage
from video_player.settings import MEDIA_ROOT
# Create your views here.


def home(request):
    video_list = Video.objects.filter(video_active=True)
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
            probe_results = probe_video(loc / filename)
            asset = Asset(asset_name=uploaded_file.name, asset_video=video, asset_codec=probe_results[0],
                          asset_duration=probe_results[1], asset_dimension_y=probe_results[2],
                          asset_dimension_x=probe_results[3])
            asset.save()
            return redirect('startube:video_properties', id=id)
    else:
        form = AddAssetFileForm()
    return render(request, 'video_properties.html', {'title': 'Uređivanje', 'video': video, 'assets': assets, 'form': form})


def remove_asset(request, id):
    if request.method == 'GET':
        what_to_delete = Asset.objects.get(id=id)
        parent_video_id = what_to_delete.asset_video.id
        parent_video = Video.objects.get(id=parent_video_id)
        file_to_delete = MEDIA_ROOT / parent_video.video_name / what_to_delete.asset_name
        what_to_delete.delete()
        remove_asset_file(file_to_delete)
    return redirect('startube:video_properties', id=parent_video_id)
