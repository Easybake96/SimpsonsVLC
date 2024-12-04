import os
import random
import time
from subprocess import Popen

# Directory containing videos and subtitles
directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []

def getVideos():
    global videos
    videos = []
    # Gather all .mp4 files in the directory
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))

def findSubtitle(video_path):
    # Check if a subtitle file exists for the video
    base_name = os.path.splitext(video_path)[0]
    for extension in ['.srt', '.sub', '.ass', '.vtt']:
        subtitle_path = f"{base_name}{extension}"
        if os.path.exists(subtitle_path):
            return subtitle_path
    return None  # No subtitle found

def playVideos():
    global videos
    if len(videos) == 0:
        getVideos()
        time.sleep(5)  # Wait to try loading videos again
        return
    random.shuffle(videos)  # Randomize video order
    for video in videos:
        subtitle_file = findSubtitle(video)
        if subtitle_file:
            # Use cvlc with subtitle file
            playProcess = Popen([
                'cvlc', '--fullscreen', '--no-osd', '--play-and-exit',
                '--sub-file', subtitle_file, video
            ])
        else:
            # Play without subtitles if no subtitle file found
            playProcess = Popen([
                'cvlc', '--fullscreen', '--no-osd', '--play-and-exit', video
            ])
        playProcess.wait()  # Wait for the process to complete

while True:
    playVideos()
