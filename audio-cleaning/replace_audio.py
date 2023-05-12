import os
import subprocess
import sys

def print_usage():
    print("Usage: {} <video_file.mp4> <audio_file.wav> <output>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 4:
    print("Error: Incorrect number of arguments.")
    print_usage()

video_file = sys.argv[1]
audio_file = sys.argv[2]
output_file = sys.argv[3]

if not os.path.isfile(video_file):
    print("Error: Video file '{}' does not exist.".format(video_file))
    print_usage()

if not os.path.isfile(audio_file):
    print("Error: Audio file '{}' does not exist.".format(audio_file))
    print_usage()

temp_video_file = "temp_video.mp4"
subprocess.run(["ffmpeg", "-i", video_file, "-c", "copy", "-an", temp_video_file])
output_file = output_file + ".mp4"
subprocess.run(["ffmpeg", "-i", temp_video_file, "-i", audio_file, "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", output_file])
os.remove(temp_video_file)
print("Replaced audio in video file with the new audio. New file '{}' created.".format(output_file))
