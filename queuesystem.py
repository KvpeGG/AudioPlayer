#imports
import vlc 
import os
import pynput
from pynput import keyboard
import threading



songList = []
songQueueLength = 0
nextSongQueueIndex = None


#def get_next_queue_index():
#    pass


def get_song_list(songListMain):

    global songList
    global songQueueLength

    songList = songListMain
    songQueueLength = len(songListMain)


def get_song_name_from_index(songIndex):

    global songList

    songName = songList[songIndex]
    print("This song is named: " + '"' + songName + '"')


#show_..._song functions:
def show_previous_song(songIndexQueue):
    global songListPath
    global songList
    global songQueueLength
    
    if songIndexQueue <= 0:
        songIndexQueue = 0
    print("Previous song index: " + str(songIndexQueue - 1))
    print("\n Song name: " + songList[songIndexQueue - 1])


def show_next_song(songIndexQueue):
    
    global songListPath
    global songList
    global songQueueLength

    if songIndexQueue == songQueueLength - 1:
        songIndexQueue = 0
    print("Playing Next: " + str(songIndexQueue + 1))
    print("\n Song name: " + songList[songIndexQueue + 1])
    

def show_current_song(songIndexQueue):

    global songListPath
    global songList
    global songQueueLength

    print("Currently playing: " + str(songIndexQueue))
    print("\n Song name: " + str(songList[songIndexQueue]))

#adding song/s to queue:
def add_to_queue():

    global songList

    addSongIndex = input("\n index of song to move:")

    try:
        int(addSongIndex)
    except ValueError:
        raise ValueError("Value error") from None 



    if 0 <= addSongIndex < len(songList):

        try:
            addSongName = songList.pop(addSongIndex)
            newIndex = int(songList[-1])
            songList.insert(newIndex, addSongName)
            print("song sucessfully added.")
        except ValueError:
            print("invalid integer (?)")

 

def print_song_list():

    global songList

    print("\nsongList: ")
    print(songList)


def play_next():

    global songList

    try: 
        nextSongIndex = int(input("Index for next song: "))

        if 0 <= nextSongIndex < len(songList):

            nextSongName = songList.pop(nextSongIndex)
            newIndex = nextSongIndex + 1

        songList.insert(newIndex, nextSongName)
            


    except:
        raise NotImplementedError
