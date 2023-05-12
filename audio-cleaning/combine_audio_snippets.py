import sys
import os
from pydub import AudioSegment

def print_usage():
    print("Usage: combine_audio.py <file1.wav> <file2.wav> ...")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Error: No input files provided.")
    print_usage()

filenames = sys.argv[1:]
audio_files = []

for filename in filenames:
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        print_usage()

    if not filename.lower().endswith('.wav'):
        print(f"Error: File '{filename}' is not a .wav file.")
        print_usage()

    audio_files.append(AudioSegment.from_wav(filename))


combined = sum(audio_files, AudioSegment.empty())
output_dir = '../output/'
os.makedirs(output_dir, exist_ok=True)
base_filename = os.path.basename(filenames[0]).split('-')[0]
output_filename = os.path.join(output_dir, f"{base_filename}.wav")
combined.export(output_filename, format="wav")
print(f"Audio combination complete. Combined file is located at: {output_filename}")