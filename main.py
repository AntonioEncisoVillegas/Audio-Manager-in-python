"""
app: Audio Manager
Author : Antonio Enciso Villegas
Functionality:
      -Register Albums
      -registrer songs
      -Display Catalog
"""
# Imports
from display import print_menu,clear,print_header
from album import Album
from song import Song 
import pickle 

# Globals
catalog = []

# Functions
def serialize_data():
    try:
        writter = open('songManager.data', 'wb') # Wb write binary 
        pickle.dump(catalog, writter)
        writter.close()
        print(" * Data saved!")

    except:
            print("* Error: Data was not saved!")
    
    

def deserialize_data():
    try:
        reader = open('songManager.data', 'rb') # rb Read Binary
        temp_list = pickle.load(reader)
        reader.close()

        for item in temp_list:
            catalog.append(item)
        print(f"Loaded {len(catalog)} albums")

    except:
        print("** Error: No data was loaded!")


def registrer_album():
    print_header("Registrer Album")
  
    title = input ("provide the Title : ")
    genre = input ("Provide the Genre : ")
    artist = input ("Provide the Artist Name : ")
    price = float(input ("Provide the price: "))
    release_year = int(input ("Provide the Release Year : "))

    id = 1
    if (len(catalog) > 0):
        last = catalog [-1]
        id = last.id + 1 

    album = Album(1, title, genre, artist, price, release_year)
    catalog.append(album)
    print(" Album Saved! ")

def print_catalog(show_songs):
    print_header("Your current catalog ")
    # iterate the list and print each album 
     
    for album in catalog:
        print(album) 
        
    if(show_songs):
        print("-" * 30)
        id = input("Select an Album to see its songs, or [x] to close ")
        if(id == 'x'): return
        
        try:
            # find the album with that id
            the_id = int(id)
            
            found = False 
            for album in catalog:
                if (album.id == the_id):
                    found = True
                    print_header("songs of the Album: " + album.title)
                    for song in album.songs:
                        print(song)

                    return album # return the selected album 
            
            if(not found):
                print("*Error: invalid Id,  try again ")
            
        except: 
            print("Invalid entry, try again ")

        #print the songs of album


def registrer_song():
    print_catalog(False)
    id = int (input(" Please Select an id "))

    # validate the id 

    found = False
    for album in catalog:
        if (album.id == id):
            print_header("Register a song " + album.title)
            title = input("Provide title: ")
            length_secs = input(" provide the lenght in secs : ")
            author = input ("Provide the Author: ")

            id = 1 
            if(len(album.songs)> 0):
                id = album.songs[-1].id + 1

            song = Song(1,title,length_secs,author)
            album.songs.append(song)
            

    if(not found):
        print("**Error: invalid id, try again !")

def delete_song():
    album = print_catalog(True)
    print("-" * 30 )
    id = int(input("Select the Id of the song to delete: "))

    found = False
    for song in album.songs:
        if(song.id == id):
            found = True 
            album.songs.remove(song)
            print(" Song removed! ")


    if(not found):
        print("*Error : invalid id, try again")



# Instructions 
deserialize_data()
input(" Press Enter to continue.......")

option = ''
while (option != 'q'):
    clear()
    print_menu()
    option = input("Please select an option ")

    if(option == 'q'):
        break
    if(option == '1'):
        registrer_album()
        serialize_data()

    if(option == '2'):
        registrer_song()
        serialize_data()

    if(option == '3'):
        print_catalog(True )

    if(option == '8' ):
        delete_song()
        serialize_data()

    input("Press Enter to continue...")
print("good bye!")