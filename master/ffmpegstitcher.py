import os
import ffmpeg

currentdir = os.getcwd()
ffmpegfolder = currentdir + "\\.ffmpeg"
ffmpegcheck = ffmpegfolder + "\\ffmpeg.exe"
processedfolder = currentdir + "\\.processed"

if os.path.exists(ffmpegfolder) is False or os.path.exists(processedfolder) is False:
    print("Creating necessary folders...")
    if os.path.exists(ffmpegfolder) is False:
            os.mkdir(ffmpegfolder)
    if os.path.exists(processedfolder) is False:
            os.mkdir(processedfolder)

if os.path.exists(ffmpegcheck) is True:
    print("\nThe FFmpeg install has been found.\n")
else:
    print('\nThe FFmpeg install hasn\'t been found, please download FFmpeg and place ffmpeg.exe in the ".ffmpeg" folder\n')

os.chdir(processedfolder)

def ffmpegstitcher():
    print("\nFFmpeg Stitcher v1.0 by hideNFN\n")

    while True:
        pathvideo = input("\nDrag the video file you would like to stitch:\n")
        pathvideo = pathvideo.strip('"')
        stream_video = ffmpeg.input(pathvideo)
        videoname = pathvideo.rsplit("\\")[-1]
        print("\n" + videoname + " was selected as the video.")
        
        print("\nSearching for the audio automatically...")
        possibleaudioname = "audio" + videoname
        pathaudioauto = pathvideo.replace(videoname, possibleaudioname)
        if os.path.exists(pathaudioauto) is True:
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
        except:
            print("\nGeneral processing error.")
ffmpegstitcher()