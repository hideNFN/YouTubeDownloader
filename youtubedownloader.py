import os
from pytube import YouTube

def mp4dwn():
    print("YouTube Downloader v1.0 by hideNFN\n")

    verificarefolder = os.getcwd() + "\\.files"
    if os.path.exists(verificarefolder) is False:
        print("Creating necessary folders...")
        os.mkdir(verificarefolder)

    while True:
        
        link = input("\nPaste the URL of the video you would like to download:\n")

        print("\nBeginning download...")

        try:
            yt = YouTube(link)
            yt.streams.filter(adaptive = True, file_extension = "mp4").first().download(max_retries = 2, output_path=".files")
            print( "\nVideo file was downloaded successfully.")
        except:
            print("\nError, the video file download failed.")

        try:
            yt = YouTube(link)
            yt.streams.filter(only_audio = True).first().download(filename_prefix = "audio", max_retries = 2, output_path=".files")
            print("\nAudio file was downloaded successfully.")
        except:
            print("\nError, the audio file download failed.")

mp4dwn()