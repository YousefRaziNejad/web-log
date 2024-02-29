import os
import subprocess
import json

class Files:

    def __init__(self, path):

        self.path = path

    def get_files(self):

        dir = self.path
        return os.listdir(dir)

    def browse_files(self):

        list_videos = list()

        for file in self.get_files():

            if file.endswith(".mp4"):
                list_videos.append(self.path + file)

            if file.endswith(".avi"):
                list_videos.append(self.path + file)

            if file.endswith(".mkv"):
                list_videos.append(self.path + file)

            if file.endswith(".mov"):
                list_videos.append(self.path + file)

        return list_videos


class Videos:

    def __init__(self, list_file_video):

        self.list_file_video = list_file_video

    def check_audio_format(self):
        videos = list()
        for video_file in self.list_file_video:

            cmd = f"ffprobe -v error -select_streams a:0 -show_entries stream=channels -of json {video_file}"
            result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if result.returncode == 0:
                data = json.loads(result.stdout)
                audio_channels = data['streams'][0]['channels']

                if audio_channels == 6:
                    videos.append(video_file)

        return videos