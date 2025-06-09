
version = "0.1.0-alpha"
print("\nBurmilla Music Player " + version + "\n")

#imports
#---------------------------------------------
import time
import queuesystem
import vlc
from pynput import keyboard
import os
import random
import six
import metadata as MD


# Select startup folder
#---------------------------------------------
MetaDataDisplay = MD.MetaDataDisplay
dirList = os.listdir(MD.folder_path)

# Filter only-folders
folderList = [f for f in dirList if os.path.isdir(os.path.join(MD.folder_path, f))]

if not folderList:
    print(r"No folders found in the specified directory.")
    print(r"Please create a folder in the directory or change the path in musicPath.txt to a folder with music files.")
    print(r"You can find the musicPath.txt file in the directory: C:\Burmilla Music\musicPath.txt")
    input("Press Enter to exit...")
    exit(1)

print("Available folders:")
for i, folder in enumerate(folderList):
    print(f"{i + 1}. {folder}")

input_choice = input("Select a folder by number (or type 'exit' to quit): ")

if input_choice.lower() == 'exit':
    print("Exiting the program.")
    exit(0)
elif input_choice.isdigit():
    choice_index = int(input_choice) - 1
    if 0 <= choice_index < len(folderList):
        selected_folder = folderList[choice_index]
        mediaFolderPath = os.path.join(r"C:\Burmilla Music\Music", selected_folder)
        print(f"Selected folder: {selected_folder}")
    else:
        print("Invalid choice. Exiting the program.")
        exit(1)


# A class to handle file paths
#---------------------------------------------
class FileHandler(object): 
    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)
        
    def create(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, 'w') as f:
            f.write("")

music_file_handler = FileHandler(r"C:\Burmilla Music\musicPath.txt")

if not music_file_handler.exists():
    music_file_handler.create()


# Uses Song Names: 
#----------
fileNames = [ f for f in os.listdir(mediaFolderPath) if os.path.isfile(os.path.join(mediaFolderPath, f))]
fileNames = MD.get_sorted_file_names(mediaFolderPath)


# Display Songs in the selected folder
#---------------------------------------------
file_paths = [os.path.join(mediaFolderPath, fname) for fname in fileNames]
MD.display_metadata(file_paths)


# Get song list and initialize the player
#---------------------------------------------
queuesystem.get_song_list(fileNames)
songIndex = 0



fileNamesListLength = len(fileNames)
instance = vlc.Instance("--no-keyboard-events", "--no-xlib", "--quiet")
player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
player.set_media(vlc.Media(os.path.join(mediaFolderPath, fileNames[songIndex])))

# Set the initial volume
#--------------------------------------------
# Set the initial volume to 20%
# You can adjust this value as needed (0-100)
volume = 20
player.audio_set_volume(volume)


# Get song length
#---------------------------------------------

def get_song_length():
    global player

    player.get_media().parse_with_options(1, 0)

    while player.get_media().get_duration() < 0:
        continue

    duration_ms = player.get_media().get_duration()
    print("Song Length: " + str(duration_ms / 1000) + " seconds")
    

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

            file_path = os.path.join(mediaFolderPath, fileNames[songIndex]) 
            metadata_display = MD.MetaDataDisplay(file_path)                            #            MD.MetaDataDisplay(file_path).display_metadata()
            currentSongName = metadata_display.display_metadata()
            if not currentSongName == None and not currentSongName == "":
                print("Now playing: " + currentSongName + "\n")

    elif key == keyboard.Key.end:
            
            player.stop()
            songIndex -= 1
            if songIndex < 0:
                songIndex = 0
            player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
            player.play()

            file_path = os.path.join(mediaFolderPath, fileNames[songIndex]) 
            metadata_display = MD.MetaDataDisplay(file_path)
            currentSongName = metadata_display.display_metadata()
            if not currentSongName == None and not currentSongName == "":
                print("Now playing: " + currentSongName + "\n")


    elif key == keyboard.Key.shift_r: #shows next song. 

        queuesystem.show_next_song(songIndex)

    elif key == keyboard.Key.ctrl_r: #shows previous song. 

        queuesystem.show_previous_song(songIndex)

    elif key == keyboard.Key.scroll_lock:  #shows current song. 
        
        queuesystem.show_current_song(songIndex)
        get_song_length()
    
    elif key == keyboard.Key.f4:

        
        queuesystem.add_to_queue()

    elif key == keyboard.Key.f5:
        file_paths = [os.path.join(mediaFolderPath, fname) for fname in fileNames]
        MD.display_metadata(file_paths)



#--------------------------------------------
def is_ended():
    global songIndex
    global player
    global fileNames

    while True:  
        if player.get_state() == vlc.State.Ended:
            print("The song has ended, skipping to the next song.")

            file_path = os.path.join(mediaFolderPath, fileNames[songIndex]) 
            metadata_display = MD.MetaDataDisplay(file_path)
            currentSongName = metadata_display.display_metadata()
            if not currentSongName == None and not currentSongName == "":
                print("Now playing: " + currentSongName + "\n")

            songIndex += 1
            if songIndex >= fileNamesListLength:
                songIndex = 0
            player = vlc.MediaPlayer(os.path.join(mediaFolderPath, fileNames[songIndex]))
            player.play()
        time.sleep(0.01)  # Sleep for a short time to avoid busy waiting

with keyboard.Listener(on_press=on_press) as listener:  #to do: if PyQt closes, close the keyboard listener and the program.
    is_ended()  
    listener.join()
