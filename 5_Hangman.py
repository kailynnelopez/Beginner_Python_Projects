import json
import random

f = open('songs.json')  # Opening JSON file
  
data = json.load(f)     # returns JSON object as a dictionary

# Iterating through the json list
songs = []
hints = []
for i in data['songs']: songs.append(i['title'])
for h in data['songs']: hints.append(h['artist'])
  
f.close()   # Closing file

def get_valid_song(songs):
    i = random.choice(range(len(songs)))    # Get Random Index from Songs list 
    song = songs[i]
    while "'" in song or '(' in song or "," in song:     #Remove songs that have weird characters 
        i = random.choice(range(len(songs)))
        song = songs[i] 
    hint = hints[i]     #Save corresponding artist as a hint
    return [song, hint]
    
def hangman():
    song_and_hint = get_valid_song(songs) 
    song_title = song_and_hint[0]
    hint = song_and_hint[1]
    song = song_title.lower()
    song_letters = set(song) # letters in the song
    alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '])
    used_letters = set() # what user has guessed \

    print("*******************************************************")
    print("         W E L C O M E  T O  H A N G M A N             ")
    print("*******************************************************")
    lives = int(input("How many lives do you want to start with: "))
    while lives <= 0 or isinstance(lives, int) == False:
        lives = int(input("How many lives do you want to start with: "))
        print("That was not a valid character, try again.")

    if ' ' in song_letters: song_letters.remove(' ')    # remove spaces from song
    used_letters.add(' ')   # add spaces between words 

    print("** If you would like a hint at any time, type 'hint' **")
    print("-------------------------------------------------------")
    while len(song_letters) > 0 and lives > 0:
        print('\nYou have used these letters:', ' '.join(sorted(used_letters)))   # letters used by player

        song_list = [letter if letter in used_letters else '-' for letter in song]
        print('Current title: ', ' '.join(song_list))

        user_letter = input('\nGuess a letter: ')
        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter.lower())
            if user_letter in song_letters:
                song_letters.remove(user_letter)
            else:
                lives = lives - 1 
                print(f"Letter is not in the word. You have {lives} more chances")
        elif user_letter in used_letters:  print("You have already used that character. Please try again.")
        elif user_letter == 'hint':        print("\nHINT: The Artist of the song is", hint)
        else:                              print("Invalid Character, try again.")
        print("-------------------------------------------------------")
    
    if lives == 0:
        print("\n*******************************************************")
        print('You failed, sorry. The song was', song_title)
    else:
        print("\n*******************************************************")
        print("Congrats! You guessed the song", song_title, "!!")


hangman()
