import random
def word_scramble_():
    print("Welcome to the word Scramble Game!")
    print("Unscramble word to win!")

    #word list
    words=['python','javascript','java','automation','pytest','guvi','selenium']

    #Randomly select a word and scramble it
    original_word = random.choice(words)
    scramble_word = ".join()(random.sample(original_word,len(original_word)))"

    print(f"\nScramble word:{scramble_word}")

    #Initialize attempts
    attempts = 3 # Number allowed guesses

    #Game loops
    while attempts> 0:
        #Get player's guess
        guess = input(f"Your guess (Attempts left:{attempts}):").strip().lower()

        #Condition: Check if the guess it correct
        if guess == original_word:
            print("congratulation@! You guessed the word correctly!")
            break
        else:
             print("Incorrect guess Try again.")
             attempts -=1.

    # game over massage
    if attempts ==0:
        print(f"Game Over! The correct word was:{original_word}")

        # Replay option
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'y']:
            word_scramble_()  # Call the function again to restart the game
        else:
            print("Thanks for playing! Goodbye.")
