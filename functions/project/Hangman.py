import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


def get_secret_word(filepath="words_alpha.txt"):
    playable_words = []
    try:
        with open(filepath, "r") as file:
            for line in file:
                word = line.strip().lower() 
                
                # Keep words between 4 and 8 letters long
                if 4 <= len(word) <= 8 and word.isalpha():
                    playable_words.append(word)
                    
        # This will print exactly how many words were loaded!
        print(f"[INFO] Loaded {len(playable_words)} playable words.")
        return random.choice(playable_words)
        
    except FileNotFoundError:
        print("\n[!] ERROR: Could not find 'words_alpha.txt'.")
        print("[!] Please make sure the downloaded text file is in the same folder as this script.")
        print("[!] Using a backup word so the game doesn't crash...\n")
        return "python"


lives = 6

print(logo)
chosen_word = get_secret_word()

# Simpler way to generate the initial blank placeholder
placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

game_over = False
guessed_letters = [] # Track all guesses to prevent double-penalizing

while not game_over:
    print(f"\n****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'. Try a different letter.")
        continue # Skips the rest of the loop and asks for a new guess without losing a life
        
    guessed_letters.append(guess)
    
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that letter is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word.upper()} YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])