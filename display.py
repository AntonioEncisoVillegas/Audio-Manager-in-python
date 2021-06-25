import os 
def print_menu():
    print("-" * 30 )
    print("** Audio Manager **")
    print("-" * 30)

    print("[1] Register Album")
    print("[2] Register Song")
    print("[3] Print Catalog")

    print("[5] Count all the song in the system")
    print("[6] Total $ in the catalog")
    print("[7] Delete Album") # only delete if there are no songs on it 
    print("[8] Delete song ")
    print("[9] Print the most expensive album  ")
    print("[10] print the unique categories ")



    print("[q] Quit ")
    

def clear():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    clear()
    print("-" * 30)
    print(text)
    print("-" * 30)



"""
song
id,
title
length_secs
author

1 - ask for the info
2 - create the song class
3 - create a song objet 
4 - print the object


"""