import os
from pytube import YouTube, exceptions

print("YouTube Downloader v1.0 by hideNFN\n")

verificarefolder = os.path.join(os.getcwd(), ".files")
if not os.path.exists(verificarefolder):
    print("Creating necessary folder...")
    os.mkdir(verificarefolder)

def mp4dwn():
    while True:
        link = input("\nPaste the URL of the video you would like to download:\n")

        video_downloaded = False

        try:
            yt = YouTube(link)
            print("\nBeginning video download...")
            yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path=".files")
            print("\nVideo file was downloaded successfully.")
            video_downloaded = True
        except exceptions.VideoUnavailable:
            print("\nError: The video is unavailable.")
        except Exception as e:
            print(f"\nError, the video file download failed: {e}")

        if video_downloaded:
            try:
                print("\nBeginning audio download...")
                yt.streams.filter(only_audio=True).first().download(output_path=".files", filename_prefix="audio")
                print("\nAudio file was downloaded successfully.")
            except Exception as e:
                print(f"\nError, the audio file download failed: {e}")
        else:
            print("\nSkipping audio download due to video download failure.")

mp4dwn()