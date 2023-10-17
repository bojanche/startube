from django.urls import path
from . import views

app_name = 'startube'

urlpatterns = [
    path('', views.home, name='home'),
    path('videoadmin', views.video_admin, name='video_admin'),
    path('videoproperties/<int:id>/', views.video_properties, name='video_properties'),
    path('videoproperties/<int:id>/<str:id1>', views.video_properties, name='video_properties'),
    path('removeasset/<int:id>/', views.remove_asset, name='remove_asset'),
]