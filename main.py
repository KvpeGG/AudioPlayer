#imports
import time
import PySide6
import queuesystem
import vlc
from pynput import keyboard
import os
import random


#QT <3



mediaFolderPath = '/home/kacper/Muzyka/AudioPlayer/'
fileNames = [ f for f in os.listdir(mediaFolderPath) if os.path.isfile(os.path.join(mediaFolderPath, f))]
print(fileNames)

songIndex = 0
fileNamesListLength = len(fileNames)
player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))

volume = 5
player.audio_set_volume(volume)





def get_song_length():
    global player

    player.get_media().parse_with_options(1, 0)

    while player.get_media().get_duration() < 0:
        continue

    duration_seconds = player.get_media().get_duration() * 1000
    print("Song Length: " + str(duration_seconds))
    

#controls
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

    elif key == keyboard.Key.shift_r:

        queuesystem.show_next_song(songIndex)

    elif key == keyboard.Key.ctrl_r:

        queuesystem.show_previous_song(songIndex)

    elif key == keyboard.Key.f10:  #to do: change this key to a different one for debugging.
        
        queuesystem.show_current_song(songIndex)

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
        time.sleep(0.2)


with keyboard.Listener(on_press=on_press) as listener:  #to do: if PyQt closes, close the keyboard listener and the program.
    is_ended()  
    listener.join()




