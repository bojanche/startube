from django.shortcuts import render, redirect
from .models import Video, Asset
from .forms import CreateVideoForm, AddAssetFileForm
from .utilities import *
from django.core.files.storage import default_storage
# Create your views here.


def home(request):
    video_list = Video.objects.all()
    return render(request, 'home.html', {'title': 'Home', 'video_list': video_list})


def video_admin(request):
    video_list = Video.objects.all()
    if request.method == 'GET':
        form = CreateVideoForm(request.GET)
        if form.is_valid():
            create_video_dir(str(request.GET.get('video_container_location')))
            form.save()
            return redirect('startube:video_admin')
    else:
        form = CreateVideoForm()
    return render(request, 'video_admin.html', {'title': 'Video Admin', 'video_list': video_list, 'form': form})


def video_properties(request, id):
    video = Video.objects.get(id=id)
    assets = Asset.objects.filter(asset_video=id)
    if request.method == 'POST':
        # original_post = request.POST.copy()
        # original_post['asset_video'] = video.id
        # request.POST = original_post
        # file = request.FILES['asset_file']
        # file_name = default_storage.save(file.name, file)
        # print(file, file_name)
        form = AddAssetFileForm(request.POST, request.FILES)
        if form.is_valid():
            assets_instance = form.save(commit=False)
            assets_instance.asset_video.upload_to = '20231001171042495923'
            print(assets_instance)
            assets_instance.save()
            return redirect('startube:video_properties', id=id)
    else:
        form = AddAssetFileForm()
    return render(request, 'video_properties.html', {'title': 'Uređivanje', 'video': video, 'assets': assets, 'form': form})

