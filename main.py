#imports
#from tkinter import *
import time
import queuesystem
import vlc
from pynput import keyboard
import os
import random

#window = Tk()
#lbl = Label(window, text="Testing shit", font=("Helvetica", 16))
#lbl.place(x=60, y=50)
#window.title("title")
#window.geometry("400x150+10+10")


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

    elif key == keyboard.Key.shift and key == keyboard.Key.page_up :

        volume = volume + 1
        player.audio_set_volume(volume)
        print("volume: " + str(volume))

    elif key == keyboard.Key.page_down:

        volume = volume - 5
        player.audio_set_volume(volume)
        print("volume: " + str(volume))

    elif key == keyboard.Key.shift and key == keyboard.Key.page_down:

        volume = volume - 1
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
        
        queuesystem.queue_function()

def is_ended():
    global songIndex
    global player
    global fileNames
        
    if player.get_state() == vlc.State.Ended:
        print("The song has ended, idiot." + str(fileNames(songIndex)))
        songIndex += 1
        if songIndex >= fileNamesListLength:
            songIndex = 0
        player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
        player.play()
    time.sleep(1)


with keyboard.Listener(on_press=on_press) as listener:  #to do: if tkinter closes, close the keyboard listener and the program.
    #window.mainloop()
    is_ended()  
    listener.join()




