# Audio Cleaning | Post Podcast Production
This script automates the process of converting audio from mp4 files into mp3, enhancing the audio via Adobe Podcast, then taking the output and replacing the original audio in the mp4 file.

## Outstanding Development Items
- [ ] Add support for automatically uploading to Adobe Podcast ... need to look into this more.

## Requirements
- brew install ffmpeg [ffmpeg](https://ffmpeg.org/) - Used to convert mp4 to mp3 and vice versa.
- pip3 install -r requirements.txt

## Usage
Several steps are currently required to get the audio cleaned up. The following steps are required:

- convert_mp4_to_mp3.py - Used to convert mp4 files to mp3 files. Additionally, creates a max length of 59 minutes to abide by Adobe Podcast Enhanced (60 minutes) maximum.

- combine_audio_snippets.py - Used to combine multiple audio snippets into one file.

```
python3 combine_audio_snippets.py ../output/chad-part-000\ \(enhanced\).wav ../output/chad-part-001\ \(enhanced\).wav

Audio combination complete. Combined file is located at: ../output/chad.wav
```

- replace_audio.py - Used to replace the audio in the mp4 file with the enhanced audio.

```
python3 replace_audio.py /mp4/preston.mp4 ../output/preston.wav ../output/preston
```

## Join the Conversation
[YouTube](https://youtube.com/@madblocks) <br />
[Discord](http://discord.gg/5t2g7ZRJ)