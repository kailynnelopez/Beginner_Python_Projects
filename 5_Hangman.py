import json
import random
# Opening JSON file
f = open('songs.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
songs = []
for i in data['songs']:
    songs.append(i['title'])

hints = []
for h in data['songs']:
    hints.append(h['artist'])
  
# Closing file
f.close()

#print(songs[:10], hints[:10])

def get_valid_song(songs):
    song = random.choice(songs)
    while "'" in song or '(' in song or "," in song:
        song = random.choice(songs)
    
    return song
    
def hangman():
    OGsong = (get_valid_song(songs))
    # song = song.replace(" ", "")
    song = OGsong.lower()
    song_letters = set(song) # letters in the song
    alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '])
    used_letters = set() # what user has guessed 

    lives = 10

    #add spaces between words 
    song_letters.remove(' ')
    used_letters.add(' ')

    # get user input
    while len(song_letters) > 0 and lives > 0:
        #letters used:
        print('You have used these letters:', ' '.join(used_letters))

        song_list = [letter if letter in used_letters else '-' for letter in song]
        print('Current title: ', ' '.join(song_list))

        user_letter = input('Guess a letter: ')

        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter.lower())
            if user_letter in song_letters:
                song_letters.remove(user_letter)
            else:
                lives = lives - 1 
                print(f"Letter is not in the word. You have {lives} more chances")
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid Character, try again.")
    
    if lives == 0:
        print('You failed, sorry. The song was', OGsong)
    else:
        print("You guessed the song", OGsong, "!!")


hangman()
