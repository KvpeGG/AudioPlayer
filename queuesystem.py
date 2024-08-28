#imports
import vlc 
import os
import pynput

songListPath = '/home/kacper/Muzyka/AudioPlayer/'
songList = [ f for f in os.listdir(songListPath) if os.path.isfile(os.path.join(songListPath, f))]
songQueueLength = len(songList)


#show_..._song functions:
def show_previous_song(songIndexQueue): #IMPORTANT: REDO THIS TO USE THE VLC LIBRARY FOR STATES, TO MAKE THIS FILE NOT USE songListPath 
    global songListPath                 #IMPORTANT: CUZ IT AINT GONNA WORK IN THE LONG RUN
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
    print("\n Song name: " + songList[songIndexQueue])

#adding song/s to queue:
def add_to_queue():

    pass
    

