# YouTubeDownloader
## Terminal based YouTube video downloader and separate script that converts it into an mp4 file.
### This script uses the `pytube` and `ffmpeg-python` repositories. The program creates all the needed files but you still need to download FFmpeg for everything to work.

### Usage
Place the link of a video (Public or Unlisted), it can be a part of a public/unlisted or private playlist, however it must not include a timestamp (such as "&t=87s") in the link.

Warning: Age-restricted videos cannot be downloaded with this.

### Build

You can use something like py2exe but performance is heavily impacted in regards to stitching videos with the ffmpegstitcher.py tool, I recommend running the python files directly because of that.

### Sources:

[pytube](https://github.com/pytube/pytube)

[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)

[FFmpeg website](https://ffmpeg.org/)
