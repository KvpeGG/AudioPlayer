import vlc 
import os



def queue_function():
    songListPath = '/home/kacper/Muzyka/AudioPlayer/'
    songList = [ f for f in os.listdir(songListPath) if os.path.isfile(os.path.join(songListPath, f))]
    
    
def add_song_queue():
    
    pass

    
    
    
    
