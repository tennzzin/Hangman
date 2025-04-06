# Hangman

## Overview

The Hangman Game is a classic word-guessing game implemented in Python. It randomly selects a word from an online wordlist, challenging players to guess the letters before running out of attempts. The game dynamically updates the visual representation of the hangman as incorrect guesses are made.

## Features
- **Dynamic Word Selection**: Fetches a random word from an online dictionary.
- **Interactive Gameplay**: Players receive feedback for correct, incorrect, or repeated guesses.
- **Visual Feedback**: ASCII art dynamically displays the hangman figure during gameplay.
- **Error Handling**: Detects invalid inputs (e.g., numbers or multi-character guesses) and prompts correction.
- **Win/Loss Conditions**: Determines and displays the game outcome, including the correct word if the player loses.

## How to Play
1. Clone the repository:
   - `git clone https://github.com/tennzzin/hangman.git`
   - `cd hangman`
2. Run the game:
   - `python hangman.py`
3. Follow the on-screen prompts:
   - Guess one letter at a time.
   - Avoid running out of attempts.

## Technology Stack
- **Language**: Python
- **Core Concepts**:
  - **File I/O**: Dynamically fetches words from an online source.
  - **Control Flow**: Manages game state with loops and conditionals.
  - **ASCII Art**: Enhances user experience with visual feedback.

## Skills Demonstrated
- **Data Handling**  
  Used `urllib` to fetch and process an online wordlist.
  
- **Error Management**  
  Included input validation for robust gameplay.
  
- **Game Logic**  
  Designed intuitive and user-friendly mechanics with clear win/loss criteria.

## Author

**Tenzin Chonyi** - [LinkedIn](https://www.linkedin.com/in/tenzin-chonyi)
