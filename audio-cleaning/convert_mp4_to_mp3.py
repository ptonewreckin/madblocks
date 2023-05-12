#!/usr/bin/env python3

import os
import subprocess
import sys
import json
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: {} <input_directory>".format(sys.argv[0]))
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = os.path.join(input_dir, 'audio')
Path(output_dir).mkdir(parents=True, exist_ok=True)
segment_duration = 59 * 60  # 59 minutes

for file in Path(input_dir).rglob('*.mp4'):
    filename = file.stem
    output_file_base = Path(output_dir) / '{}'.format(filename)
    output_file = '{}.mp3'.format(output_file_base)
    cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', str(file)]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    video_info = json.loads(result.stdout.decode('utf-8'))
    video_duration = float(video_info['format']['duration'])

    if video_duration <= segment_duration:
        # If the video duration is less than or equal to 59 minutes, just convert it to mp3
        subprocess.run(['ffmpeg', '-i', str(file), '-vn', '-acodec', 'libmp3lame', '-ac', '2', '-ab', '192k', '-ar', '48000', output_file])
        print("Converted '{}' to MP3.".format(filename))
    else:
        # If the video duration is more than 59 minutes, convert it to mp3 and split it into 59-minute segments
        subprocess.run(['ffmpeg', '-i', str(file), '-vn', '-acodec', 'libmp3lame', '-ac', '2', '-ab', '192k', '-ar', '48000', '-f', 'segment', '-segment_time', str(segment_duration), '{}-part-%03d.mp3'.format(output_file_base)])
        print("Converted '{}' to MP3 and split into segments.".format(filename))

print("Conversion and segmentation complete. Check the 'audio' subdirectory for the MP3 files.")
