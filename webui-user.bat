@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=

start /B python Discord_txt2img_uploader.py
start /B python Discord_img2img_uploader.py

call webui.bat
