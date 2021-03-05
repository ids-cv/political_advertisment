#!/bin/bash

if [ ! -f "audio_example.mp3" ]; then
    wget https://github.com/deezer/spleeter/raw/master/audio_example.mp3
fi
spleeter separate -o output/ audio_example.mp3
