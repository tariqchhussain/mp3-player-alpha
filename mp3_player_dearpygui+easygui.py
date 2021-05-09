# Imports

import pyglet
from pyglet import clock
from dearpygui.core import *
from dearpygui.simple import *
import time
from datetime import timedelta
#from tkinter import *
#from tkinter import filedialog
import threading
import pyglet_ffmpeg
import easygui
import sys

## Object variables

#root = Tk()
#root.withdraw()
#pyglet_ffmpeg.load_ffmpeg()
#pyglet.options['audio'] = ('directsound')
player = pyglet.media.Player()
clock = pyglet.clock.Clock()
pyglet.clock.set_default(clock)
music_source = pyglet.media.Source()

## Player functions

def song_play():
    if player.playing == False:
         player.play()
         song_duration()
    else:
         pass

def song_pause():
    if player.playing == True:
        player.pause()
    else:
        pass

def next_track():
    player.pause()
    player.next_source()
    time.sleep(1)
    player.play()

'''
def player_exit():
    keyboard.wait('ctrl+e')
    print("Player will exit in 5 seconds...")
    time.sleep(5)
    print("Exiting...")
    sys.exit()
'''
def gui_exit():
    print("Program exiting...")
    time.sleep(0.5)
    sys.exit()

def file_open():
    #root.update()
    #root.deiconify()
    new_song = easygui.fileopenbox(msg="Choose another file", default=r'D:\User Files\Music\\')
    track2 = pyglet.media.load(new_song)
    player.queue(track2)
    print('Song added to playlist!')
    new_song = new_song.split("/")[-1].strip('.mp3')
    song_title_2 = f"Now Playing:\n\n{new_song}"
    set_value('title', song_title_2)



## Function to pull current song duration from pyglet

# player.time is stored as a float, and prints in seconds instead of minutes (i.e it will print 90 instead of 1:30)...
def song_duration(*args):
 
    duration = int(player.time) / 60         # ...so the duration variable will take that value and divide it by 60 (converting seconds to minutes)       
    time_count = timedelta(minutes=duration) # stores the reformatted float in a new variable
    if player.playing == True:               # checks if the player is playing music
        print(time_count)  
        set_value('time', time_count)                  # prints the current (reformatted) time in dearpygui
    else:
        pass

#def duration_thread():
    d = threading.Thread(name='daemon1', target=song_duration, daemon=True)
    d.start()



## Main program

ffmpeg = pyglet.media.have_ffmpeg()
print(ffmpeg)
mp3_file = easygui.fileopenbox(msg="Choose a file", default=r'D:\User Files\Music\\')
song = pyglet.media.StaticSource(pyglet.media.load(mp3_file))
player.queue(song)
mp3_file = mp3_file.split("/")[-1].strip('.mp3')
song_title = f"Now Playing:\n\n{mp3_file}"
#s_time = song_duration()

# Functions for dearpygui window

set_main_window_size(580, 340)
#set_start_callback(duration_thread)
set_exit_callback(gui_exit)
set_style_window_padding(180, 60)
set_style_window_title_align(0.5, 0.5)

with window('MP3 Player', width=540, height=280):
    print("GUI is initialised...")
    set_window_pos('MP3 Player', 0, 0)
    add_text('MP3 Player, powered by Pyglet')
    add_spacing(count=5)
    add_text(name='title', default_value=song_title)
    add_spacing(count=5)
    add_button('Play', callback=song_play)
    add_same_line(spacing=1)
    add_button('Pause', callback=song_pause)
    add_same_line(spacing=1)
    add_button('Add song', callback=file_open)
    add_button('Next song', callback=next_track)
    add_text(name='time')

#root.mainloop()
start_dearpygui(primary_window='MP3 Player')
pyglet.app.run()


### to-do list
## find out how to close tkinter after second use (impossible, probably...) - DONE! Switched to easygui
## add time to the GUI - DONE!
    ## fix choppy audio playback(!!!)
# add a feature where the song_title variable updates with a new song(?) - DONE!
## find new inspiration for features from other projects

## Fully switch to tkinter!!