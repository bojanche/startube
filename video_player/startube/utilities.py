import os
from video_player.settings import MEDIA_DIR


def create_video_dir(name):
    path = os.getcwd()+'\\'+MEDIA_DIR+'\\'+name
    os.mkdir(path)