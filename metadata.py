from tinytag import TinyTag as tinytag
import os



#--------------------------------------------
class MetaDataDisplay(): # A class to handle metadata display for music files
    def __init__(self, file_path):
        self.file_path = file_path
        self.metadata = self.get_metadata()
    
    def get_metadata(self):

        try:
            tag = tinytag.get(self.file_path)
            if not tag:
                print(f"No metadata found for {self.file_path}")
                return None

            metadata = {
                'title': str(tag.title),
                'album': str(tag.album) if tag.album else None,
                'track': str(tag.track) if tag.track else None,
                'artist': str(tag.artist) if tag.artist else None,
                'duration': str(tag.duration) if tag.duration else None,
                'year': str(tag.year) if tag.year else None
            }
            return metadata

        except Exception as e:
            print(f"Error processing {self.file_path}: {e}")
            return None
    
    def display_metadata(self):
            if not self.metadata:
                print(f"No metadata available for {self.file_path}")
                return
            metadata = self.metadata
            for _, file_path in file_metadata:
                print(metadata["title"])
                print("\n")
    
    def display_metadata(self):
        if not self.metadata:
            print(f"No metadata available for {self.file_path}")
            return
        
        if self.metadata['title']:
            return self.metadata['title']


try:

    f = open(r"C:\Burmilla Music\musicPath.txt", "r")
    folder_path = f.read().strip()
    f.close()
    fileNames = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    #print(fileNames)

except FileNotFoundError:
    print(r"Restart the program and enter a valid music path in the file 'musicPath.txt' located in 'C:\Burmilla Music\'.")
    print("If the file does not exist, it will be created automatically.")
    print(r"Default path is C:\Burmilla Music\Music")
    print("You can change the path by editing the 'musicPath.txt' file.")
    print("Or put your music files in the Music folder.")

    os.makedirs(r"C:\Burmilla Music", exist_ok=True)
    os.makedirs(r"C:\Burmilla Music\Music", exist_ok=True)
    open(r"C:\Burmilla Music\musicPath.txt", "a")
    f = open(r"C:\Burmilla Music\musicPath.txt", "w")
    f.write(r"C:\Burmilla Music\Music")
    f.close()
    input("Press Enter to exit...")
    exit(1)


# Gather metadata for sorting
file_metadata = []
for each_file in fileNames:
    file_path = os.path.join(folder_path, each_file)
    tag = tinytag.get(file_path)
    track_num = tag.track if tag and tag.track is not None else float('inf')
    file_metadata.append((track_num, file_path))

# Sort by track number using list.sort()
def sorting_key(x):
    if isinstance(x[0], (int, float)):
        return x[0]
    else:
        return float('inf')  

file_metadata.sort(key=sorting_key)

# Display for terminal 
#---------------------------------------
def display_metadata(file_path_list):
    try:
        if not file_path_list:
            print("No files to display.")
            return

        print("\nAlbum:", MetaDataDisplay(file_path_list[0]).metadata.get("album", "Unknown"), "\n")

        for i, path in enumerate(file_path_list, 1):
            if os.path.isfile(path):
                meta = MetaDataDisplay(path)
                metadata = meta.metadata
                title = metadata.get("title", "Unknown Title")
                print(f"{i}. {title}")
        print("\n")
    except Exception as e:
        print(f"An error occurred: {e}")

#---------------------------------------
def get_sorted_file_names(folder_path):
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    file_metadata = []

    for file_name in file_names:
        full_path = os.path.join(folder_path, file_name)
        tag = tinytag.get(full_path)
        track_num = tag.track if tag and tag.track is not None else float('inf')
        file_metadata.append((track_num, file_name))

    file_metadata.sort(key=lambda x: x[0] if isinstance(x[0], (int, float)) else float('inf'))
    sorted_file_names = [file_name for _, file_name in file_metadata]

    return sorted_file_names


