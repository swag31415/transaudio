@echo off
for %%i in (*.mp4) do ffmpeg -i "%%i" -q:a 0 -map a "%%~ni.flac"