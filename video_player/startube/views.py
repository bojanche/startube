from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'home.html', {'title': 'Home'})


def video_admin(request):
    return render(request, 'video_admin.html', {'title': 'Video Admin'})
