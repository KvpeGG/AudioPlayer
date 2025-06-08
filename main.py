#imports
import time
import queuesystem
import vlc
from pynput import keyboard
import os
import random
import six

#QT <3

# Default file path: /home/kacper/Muzyka/Dark Times/
#--------------------------------------------
f = open("musicpath.txt", "r")
mediaFolderPath = f.read().strip()
f.close()

#--------------------------------------------


fileNames = [ f for f in os.listdir(mediaFolderPath) if os.path.isfile(os.path.join(mediaFolderPath, f))]
print(fileNames)

queuesystem.get_song_list(fileNames)


songIndex = 0
fileNamesListLength = len(fileNames)
instance = vlc.Instance("--no-keyboard-events", "--no-xlib", "--quiet")
player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
player.set_media(vlc.Media(os.path.join(mediaFolderPath, fileNames[songIndex])))


volume = 5
#player.audio_set_volume(volume)



def get_song_length():
    global player

    player.get_media().parse_with_options(1, 0)

    while player.get_media().get_duration() < 0:
        continue

    duration_seconds = player.get_media().get_duration() * 1000
    print("Song Length: " + str(duration_seconds))
    

# Controls
#--------------------------------------------
def on_press(key):
    global volume
    global player
    global songIndex
    global fileNamesListLength

    if volume < 0:
        volume = 0
    elif volume > 100:
        volume = 100

    elif key == keyboard.Key.insert:
        
        player.play()

        if key== keyboard.Key.insert:
            player.pause()

    elif key == keyboard.Key.page_up:

        volume = volume + 5
        player.audio_set_volume(volume)
        print("volume: " + str(volume))

    elif key == keyboard.Key.page_down:

        volume = volume - 5
        player.audio_set_volume(volume)
        print("volume: " + str(volume))

    elif key == keyboard.Key.home:

            player.stop()
            songIndex += 1
            if songIndex >= fileNamesListLength:
                songIndex = 0

            player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
            player.play()

    elif key == keyboard.Key.end:
            
            player.stop()
            songIndex -= 1
            if songIndex < 0:
                songIndex = 0
            player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
            player.play()

    elif key == keyboard.Key.shift_r: #shows next song. 

        queuesystem.show_next_song(songIndex)

    elif key == keyboard.Key.ctrl_r: #shows previous song. 

        queuesystem.show_previous_song(songIndex)

    elif key == keyboard.Key.scroll_lock:  #shows current song. 
        
        queuesystem.show_current_song(songIndex)
    
    elif key == keyboard.Key.f4:

        
        queuesystem.add_to_queue()

    elif key == keyboard.Key.f5:
        queuesystem.print_song_list()

#--------------------------------------------

def is_ended():
    global songIndex
    global player
    global fileNames

    while True:  
        if player.get_state() == vlc.State.Ended:
            print("The song has ended, idiot.")
            songIndex += 1
            if songIndex >= fileNamesListLength:
                songIndex = 0
            player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
            player.play()
        time.sleep(0.05)


with keyboard.Listener(on_press=on_press) as listener:  #to do: if PyQt closes, close the keyboard listener and the program.
    is_ended()  
    listener.join()




