from youtube_search import YoutubeSearch
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import concatenate_audioclips
import sys
import os
sys.argv
x = sys.argv[1]
n = int(sys.argv[2])
t = int(sys.argv[3])
l=sys.argv[4]
results = YoutubeSearch(x, max_results=n).to_dict()
d = []
for i in range(n):
    d.append("youtube.com"+results[i]['url_suffix'])
print(d)
for i in range(n):
    vid = YouTube(d[i])
    Yvideo = vid.streams.filter(
        file_extension='mp4', progressive=True).order_by('resolution').desc()

    Yvideo.get_lowest_resolution().download('~/Downloads')
# the directory where the video files are located
video_dir = "D:\synthea.wiki\~\Downloads"
# the directory where the audio files will be saved
audio_dir = "D:\synthea.wiki\Audio Files"

# loop through all the files in the video directory
for filename in os.listdir(video_dir):
    # check if the file is a video file
    if filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi"):
        # create a VideoFileClip object
        video = VideoFileClip(os.path.join(video_dir, filename))
        # extract the audio from the video
        audio = video.audio
        # save the audio to a file
        audio.write_audiofile(os.path.join(
            audio_dir, filename.split(".")[0] + ".mp3"))

# print("All videos have been converted to audio!")
audio_dir = "D:\synthea.wiki\Audio Files"
# the directory where the trimmed audio files will be saved
trimmed_audio_dir = "D:\synthea.wiki\Trims"

# loop through all the files in the audio directory
for filename in os.listdir(audio_dir):
    # check if the file is an audio file
    if filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".flac"):
        # create an AudioFileClip object
        audio = AudioFileClip(os.path.join(audio_dir, filename))
        # trim the first t seconds from the audio
        trimmed_audio = audio.subclip(0, t)
        # save the trimmed audio to a file
        trimmed_audio.write_audiofile(
            os.path.join(trimmed_audio_dir, filename))

# print("All audio files have been trimmed!")
# the directory where the audio files are located
audio_dir = "D:\synthea.wiki\Trims"
# the file where the joined audio will be saved
joined_audio_file = "D:\synthea.wiki/"+l

# create an empty list to store the audio clips
audio_clips = []

# loop through all the files in the audio directory
for filename in os.listdir(audio_dir):
    # check if the file is an audio file
    if filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".flac"):
        # create an AudioFileClip object and add it to the list of audio clips
        audio_clips.append(AudioFileClip(os.path.join(audio_dir, filename)))

# concatenate all the audio clips
joined_audio = concatenate_audioclips(audio_clips)

# save the joined audio to a file
joined_audio.write_audiofile(joined_audio_file)

print("All audio files have been joined!")
