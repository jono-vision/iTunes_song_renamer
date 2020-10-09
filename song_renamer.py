#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:44:47 2020

@author: jonathandown
"""

"""
iTunes id3 tag renamer to remove featured artists in the artist tag and all columns are correctly tabulated
"""

from mutagen.mp4 import MP4
import requests, os
directory = '/Volumes/Media Drive/iTunes/iTunes Media/Music/Compilations/Special Occasion'
os.chdir(directory)

artist_name = ''

for folder,subfolder,filenames in os.walk(directory):
    #file = '09 In Distress.m4a'
    for file in filenames:
        audio = MP4(file)
        song=audio['©ART'][0].split()
        song+=audio['©nam'][0].split()
        site = 'https://itunes.apple.com/search?term=' + '+'.join(song) + '&limit=1'
        text = ' '.join(song)

        res = requests.get(site)
        try:
            res.raise_for_status()
            if len(res.json()['results']) == 0:
                print(f'No result found for {text}')
            else:
                info = res.json()['results'][0]
                audio['©ART'] = info['artistName']
                audio['©nam'] = info['trackName']
                audio['©day'] = info['releaseDate']
    
        except Exception as exc:
            print(f'There was an issue with song: {text}')
    
        audio.save(file)


    
    