# YouTube mp3 and mp4 Downloader

# Import the necessary libraries
from pytube import YouTube
from moviepy.editor import *
import os

# User-selectable video download or audio conversion function from a YouTube URL
def download_video(url, choice):
    video = YouTube(url)  # creating a video with YouTube URL
    
    if choice == 'mp3':  # checking if the user wants to download the audio (mp3)
        streams = video.streams.filter(only_audio=True)  # filtering available to only audio
        
        found = False  # Initializing a variable to track if audio is found
        
        for stream in streams:  # iterating through available audio
            found = True  # marking the presence of a audio
            print("Converting to mp3...")  # indicating the conversion process to MP3
            
            # Downloading the audio as an mp4 file and creating the corresponding MP3 file
            mp4_file = stream.download()
            mp3_file = mp4_file.split(".mp4")[0] + ".mp3"
            video_clip = AudioFileClip(mp4_file)
            video_clip.write_audiofile(mp3_file)
            video_clip.close()  # closing the video clip
            os.remove(mp4_file)  # remove the temporary mp4 file
            print("mp3 download completed.")  # show mp3 download complete
            break  # exit the loop after processing the first available audio
        
        if not found:  # if no audio is found
            print("Audio stream not found.")  # notify the user
            
    elif choice == 'mp4':  # Checking if the user wants to download the video (MP4)
        stream = video.streams.get_highest_resolution()  # get the video with the highest resolution
        
        if stream:  # if a video is available
            print(f"{stream.resolution} downloading resolution video...")  # indicate the resolution of the video being downloaded
            stream.download()  # download the video
            print("Video download complete.")  # notify completion of the video download
        else:  # if no video stream is found
            print("Video not found.")  # notify the user
            
    else:
        print("Invalid choice. Please enter 'mp3' or 'mp4'.")   # reports an invalid selection if the user input is not mp3 or mp4.

# Main program execution
if __name__ == "__main__":
    url = input("Enter the URL of the YouTube video you want to download: ")  # request YouTube URL from the user
    download_type = input("Enter 'mp3' or 'mp4' to choose the download type: ")  # request the download type from the user
    download_video(url, download_type)  # call the download_video function with user inputs