'''resolve.py'''

"""
Export an XML file that can be imported by DaVinci Resolve.
"""

# Included functions
from usefulFunctions import conwrite

# Internal libraries
import os

# movie
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def exportSplit(myInput, output, clips, duration, sampleRate, audioFile, log):
    filepath = os.path.abspath(myInput)
    name = os.path.basename(myInput)

    # Handle clips.
    print(f'[\n')

    total = 0
    for j, clip in enumerate(clips):
        print('{ \n')

        myStart = int(total)
        total += (clip[1] - clip[0]) / (clip[2] / 100)
        myEnd = int(total)

        print(f'"clipitem": {j}, \n')
        print(f'"name": "{name}", \n')
        print(f'"filepath": "{filepath}", \n')
        print(f'"duration": {duration}, \n')

        print(f'"start": {myStart}, \n')
        print(f'"end": {myEnd}, \n')

        _in = int(clip[0] / (clip[2] / 100))
        _out = int(clip[1] / (clip[2] / 100))

        print(f'"in": {_in}, \n')
        print(f'"out": {_out}, \n')

        targetname = os.path.splitext(filepath)[0] + f"_ALTERED_{j}.mov"
        ffmpeg_extract_subclip(filepath, _in/29.97, _out/29.97, targetname=targetname)
        # Linking for video blocks
        print('}\n')

    conwrite('')
