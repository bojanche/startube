from django.shortcuts import render, redirect
from .models import Video, Asset
from .forms import CreateVideoForm

# Create your views here.


def home(request):
    video_list = Video.objects.all()
    return render(request, 'home.html', {'title': 'Home', 'video_list': video_list})


def video_admin(request):
    video_list = Video.objects.all()
    if request.method == 'GET':
        print('tu sam')
        form = CreateVideoForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('startube:video_admin')
    else:
        form = CreateVideoForm()
    return render(request, 'video_admin.html', {'title': 'Video Admin', 'video_list': video_list, 'form': form})

