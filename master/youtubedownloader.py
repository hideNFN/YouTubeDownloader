import os
import ffmpeg
from pytube import YouTube, exceptions

def menu():
    choice = input("1.) YouTube Downloader\n2.) FFmpeg Stitcher\n")
    if choice == "1":
        mp4dwn()
    if choice == "2":
        ffmpegstitcher()
    else:
        return


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.mkdir(folder_path)

def check_ffmpeg_install(ffmpeg_check_path):
    if os.path.exists(ffmpeg_check_path):
        print("\nThe FFmpeg install has been found.\n")
    else:
        print('\nThe FFmpeg install hasn\'t been found, please download FFmpeg and place ffmpeg.exe in the ".ffmpeg" folder\n')

def mp4dwn():
    create_folder(verificarefolder)
    
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

def ffmpegstitcher():
    create_folder(ffmpegfolder)
    check_ffmpeg_install(ffmpegcheck)
    create_folder(processedfolder)
    os.chdir(processedfolder)

    while True:
        pathvideo = input("\nDrag the video file you would like to stitch:\n")
        pathvideo = pathvideo.strip('"')
        stream_video = ffmpeg.input(pathvideo)
        videoname = pathvideo.rsplit("\\")[-1]
        print("\n" + videoname + " was selected as the video.")
        
        print("\nSearching for the audio automatically...")
        possibleaudioname = "audio" + videoname
        pathaudioauto = pathvideo.replace(videoname, possibleaudioname)
        if os.path.exists(pathaudioauto):
            print("\nAudio file has been found.")
            stream_audio = ffmpeg.input(pathaudioauto)
        else:
            selectedaudiopath = input("\nThe audio file hasn\'t been found, drag the audio file:\n")
            selectedaudiopath = selectedaudiopath.strip('"')
            stream_audio = ffmpeg.input(selectedaudiopath)
            audioname = selectedaudiopath.rsplit("\\")[-1]
            print("\n" + audioname + " was selected as the audio.")

        try:
            videoname = os.path.splitext(videoname)[0]
            ffmpeg.concat(stream_video, stream_audio, v=1, a=1).output(videoname + ".mp4").run(cmd=ffmpegcheck)
            print("\nThe video was processed successfully.")
        except Exception as e:
            print(f"\nError: {e}")

print("YouTube Downloader v1.0 by hideNFN\n")

verificarefolder = os.path.join(os.getcwd(), ".files")
ffmpegfolder = os.path.join(os.getcwd(), ".ffmpeg")
ffmpegcheck = os.path.join(ffmpegfolder, "ffmpeg.exe")
processedfolder = os.path.join(os.getcwd(), ".processed")

menu()