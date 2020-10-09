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
directory = '/Volumes/Media Drive/iTunes/iTunes Media/Music/Compilations/JESUS IS KING'
os.chdir(directory)

splitter_list = ['feat.', 'ft.', 'featuring','Feat.', 'Ft.', 'Featuring', 'feat', 'Feat']
artist_name = ''

for folder,subfolder,filenames in os.walk(directory):
    
    for file in filenames:
        audio = MP4(file)
        artist = audio['©ART'][0]
        splitter = list(set(artist.split()) & set(splitter_list)) # Find the variant of feature used
        
        if splitter == []: #If there is no featured artist in the artist tag skip to next file
            continue
        splitter = splitter[0].center(len(splitter)+2) #pads the string is spaces
        split_artist = artist.split(splitter)
        featured_artist = split_artist[1]

        if artist_name == '': # first file
            artist_name = split_artist[0]
        
        audio['©nam'] =  audio['©nam'][0] + ' (ft.' + featured_artist + ')'
        audio['©ART'] = artist_name
        audio.save(file)


    
    