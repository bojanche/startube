from django.urls import path
from . import views

app_name = 'startube'

urlpatterns = [
    path('', views.home, name='home'),
]