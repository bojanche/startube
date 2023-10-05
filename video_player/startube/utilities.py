import os
# from video_player.settings import MEDIA_DIR
from ffprobe import FFProbe


# def create_video_dir(name):
#     path = os.path.join(MEDIA_DIR, name)
#     os.mkdir(path)


def probe_video(in_file):
    metadata = FFProbe(in_file)
    codec = metadata.streams[0].codec_name
    duration = metadata.streams[0].duration_seconds()
    return [codec, duration]
