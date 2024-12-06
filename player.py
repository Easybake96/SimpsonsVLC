import os
import random
import time
from subprocess import Popen

# Directory containing videos
directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []

def getVideos():
    global videos
    videos = []
    # Gather all .mp4 files in the directory
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))

def playVideos():
    global videos
    if len(videos) == 0:
        getVideos()
        time.sleep(5)  # Wait to try loading videos again
        return
    random.shuffle(videos)  # Randomize video order
    for video in videos:
        # Use mpv to play videos
        playProcess = Popen([
            'mpv', '--fullscreen', '--no-osd', '--loop-file=no', video
        ])
        playProcess.wait()  # Wait for the process to complete

while True:
    playVideos()

