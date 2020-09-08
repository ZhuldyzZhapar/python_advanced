# Write a game, where the user has to guess a word

hint = "What would you use to play Doom-2?"
the_word = "computer"
game_over = False
board = list("*" * len(the_word))
while not game_over:
    print("")
    print("------------------------------")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint: {hint}")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    if len(user_guess) == 1:
        for i in range(len(the_word)):
            if the_word[i] == user_guess:
                board[i] = user_guess
    else:
        if user_guess == the_word:
            print("Correct! Congratulations!")
            game_over = True
        else:
            print("Incorrect, think again.")

# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.
