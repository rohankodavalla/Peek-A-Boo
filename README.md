# PEEK-A-BOO Memory Game

**Description:**

In this assignment, you will gain experience with the Python programming language, a dynamically typed, easy-to-use, Object-Oriented language. You will develop a simple console-based game to test players' memory using basic objects and various Python data structures.

-------------------------------------------------------------------------------------------------------------------------------------------------

## Game Overview

The game displays a square grid with columns labeled by letters and rows by numbers. The grid contains pairs of integers hidden behind 'X' symbols. The player's goal is to find the hidden pairs with the fewest guesses possible. A simple menu allows interaction with the game.

-------------------------------------------------------------------------------------------------------------------------------------------------

## Features

- **Grid Display**: Columns are labeled with letters (e.g., A, B, C) and rows with numbers (e.g., 0, 1, 2).
- **Hidden Numbers**: The grid initially displays 'X' symbols, hiding the numbers.
- **Menu Options**:
  1. Select a pair of cells to reveal.
  2. Reveal a single cell.
  3. Give up and reveal the entire grid.
  4. Start a new game.
  5. Exit the game.

-------------------------------------------------------------------------------------------------------------------------------------------------

## Gameplay

1. **Initialization**: The grid is initialized with pairs of integers randomly distributed.
2. **Guessing**: Players select cells to reveal their contents. If a pair is not matched, the cells are hidden again after 2 seconds. Matched pairs remain visible.
3. **Manual Reveal**: Players can reveal a single cell using the appropriate menu option.
4. **Winning**: The player wins by finding all pairs. The score is calculated based on the number of guesses compared to the minimum possible guesses.

-------------------------------------------------------------------------------------------------------------------------------------------------

## Score Calculation

The score is a number between 0 and 100, calculated as:

\[ \text{Score} = \left( \frac{\text{minimum\_possible\_guesses}}{\text{actual\_guesses}} \right) \times 100 \]

- Using Menu Option 2 counts as two guesses.
- The score will always be greater than 0 if at least one valid guess is made.

-------------------------------------------------------------------------------------------------------------------------------------------------

## Grid Sizes

The game can be played with a 2x2, 4x4, or 6x6 grid, specified as a command-line argument.

## Error Checking

1. **Command Line Argument**: Ensure a valid grid size (2, 4, or 6) is specified.
2. **Menu Option Selection**: Must be a number between 1 and 5.
3. **Cell Coordinates**: Verify the column (letter) and row (number) are valid. Players cannot select the same cell twice in one guess.

-------------------------------------------------------------------------------------------------------------------------------------------------

## Usage

-  python peek_a_boo.py [grid_size]
   grid_size: Size of the grid (2, 4, or 6).

   
