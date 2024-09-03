#imports
import vlc 
import os
import pynput



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
    print("\n Song name: " + songList[songIndexQueue])

#adding song/s to queue:
def add_to_queue():
    global songList

    try:
        addSongIndex = int(input("Index for the next song: "))

        if 0 <= addSongIndex < len(songList):
            
            addSongname = songList.pop(addSongIndex)
            newIndex = int(input("Enter the new position: "))

            if 0 <= newIndex < len(songList):
                
                songList.insert(newIndex, addSongname)
                print("Bravo, you did it! You twat... :3")
            
            else:
                
                print("New index out of range.")
                songList.insert(addSongIndex, addSongname)
        else:
            
            print("Index out of range.")
            
    except ValueError:
        
        print("Invalid interger.")
 

def print_song_list():

    global songList

    print(songList)

