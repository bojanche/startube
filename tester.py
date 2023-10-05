# from ffprobe import FFProbe
#
# metadata = FFProbe('waiting.mp4')
#
# for stream in metadata.streams:
#     if stream.is_video():
#         print('Stream contains {} frames.'.format(stream.codec()))

from video_player.startube.utilities import probe_video


fajl = probe_video('waiting.mp4')
print(type(fajl[1]))