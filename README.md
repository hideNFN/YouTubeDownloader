# YouTubeDownloader
## Terminal based YouTube video downloader and separate script that converts it into an mp4 file.
### This script uses the `pytube` and `ffmpeg-python` repositories and has a freeze.py file with `py2exe` build instructions. The program creates all the needed files but you still need to download FFmpeg for everything to work.

### Usage
Place the link of a video (Public or Unlisted), it can be a part of a public/unlisted or private playlist, however it must not include a timestamp (such as "&t=87s") in the link.

Warning: Age-restricted videos cannot be downloaded with this.

NOTE: Make sure to keep `pytube` updated at all times (with the "pip install --upgrade pytube" command) since YouTube purposefully blocks it occasionally.

### Build

Use the `python freeze.py` command.

PSA: If py2exe is used, performance is heavily impacted in regards to stitching videos with the ffmpegstitcher.exe tool, I recommend running the python files directly if you want the results as fast as possible.

### Sources:

[pytube](https://github.com/pytube/pytube)

[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)

[FFmpeg website](https://ffmpeg.org/)

[py2exe](https://github.com/py2exe/py2exe)