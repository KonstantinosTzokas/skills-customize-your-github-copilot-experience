# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the core game state and choose a random secret word from a predefined list.

#### Requirements
Completed program should:

- Define a list of candidate words (e.g. `['python', 'coding', 'hangman', 'computer']`).
- Randomly pick one word for the current round using `random.choice`.
- Initialize a representation of the guessed word with underscores for unguessed letters (e.g. `_ _ _ _ _`).
- Track letters guessed so far.

### 🛠️ Guess Processing and Game Loop

#### Description
Process player guesses in a loop until victory or defeat.

#### Requirements
Completed program should:

- Prompt the user to guess a single letter using `input()`.
- Ignore repeated guesses and notify the player if they guess the same letter again.
- Update the display representation when correct letters are guessed.
- Decrement remaining attempts for incorrect guesses.
- Show current progress after each guess (e.g. `p _ t h _ n`).
- Limit the number of incorrect guesses (e.g. 6 attempts).

### 🛠️ End Conditions and Messaging

#### Description
Display win/lose results and wrap up the game.

#### Requirements
Completed program should:

- End the game with a win message when the word is fully guessed.
- End with a lose message when guesses run out and reveal the secret word.
- Print the final number of correct and incorrect guesses.
- Allow the player to play again (optional enhancement).


## 💡 Starter Code

See `assignments/games-in-python/starter-code.py` for a scaffold you can use as a starting point.

## 📌 Skills practiced

- String manipulation
- Conditional logic
- Loops
- Random selection
- User input validation
