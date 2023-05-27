import sys
import string
import random
import time
from os import system

# Function to initialize the grid
def initialize_grid(size):
    grid = []
    nums = list(range(1, size * size // 2 + 1)) * 2
    random.shuffle(nums)

    for _ in range(size):
        row = []
        for _ in range(size):
            num = nums.pop()
            row.append(num)
        grid.append(row)

    return grid

# Function to get the row and column indices from cell coordinates
def get_coordinates(cell):
    column = cell[0].upper()
    row = int(cell[1:])
    col_index = string.ascii_uppercase.index(column)
    return row, col_index

# Function to display the grid
'''
def display_grid(grid):
    size = len(grid)
    print("  " + "  ".join(string.ascii_uppercase[:size]))
    column_labels = "   ".join([f"{label} " for label in string.ascii_uppercase[:size]]) 
   # print("+" + "-" * (2 * size + 1) + "+")

    for i, row in enumerate(grid):
        #print(f"{i} | {' '.join(map(str, row))} |")
        ####### this works print(f"{i}  {'  '.join(['[' + str(cell) + ']' for cell in row])}")
        formatted_row = "  ".join([f"[{cell}]" for cell in row])
        print(f"{i}  {formatted_row}")


    #print("+" + "-" * (2 * size + 1) + "+")
'''

def display_grid(grid):
    size = len(grid)
    column_labels = " ".join([f"{' ' * 2}{label}{' ' * 2}" for label in string.ascii_uppercase[:size]])

    print()
    print(column_labels)
    print()

    for i, row in enumerate(grid):
        formatted_row = "  ".join([f"[{cell}]" for cell in row])
        print(f"{i}  {formatted_row}")
        print()


# Function to play the game
# Function to play the game

def play_game(size):
    grid = initialize_grid(size)
    hidden_grid = [['X' for _ in range(size)] for _ in range(size)]
    hidden_grid_1 = [[False for _ in range(size)] for _ in range(size)]

    attempts = 0
    guessed_pairs = set()
    #print("before while")
    while True:
        print("------------------------")
        print("|      PEEK-A-BOO      |")
        print("------------------------")
        print("\n")
        display_grid(hidden_grid)
        print("\n")
        print("Menu:")
        print("1. Let me select two elements")
        print("2. Uncover one element for me")
        print("3. I give up - reveal the grid")
        print("4. New game")
        print("5. Exit")

        option = input("Enter your option: ")

        if option == '1':
            print("Enter the coordinates of the first cell (e.g., A0):")
            cell1 = input()
            print("Enter the coordinates of the second cell (e.g., B2):")
            cell2 = input()

            row1, col1 = get_coordinates(cell1)
            row2, col2 = get_coordinates(cell2)

            if cell1 == cell2:
                print("Please enter two different cells.")
                continue

            if row1 >= size or col1 >= size or row2 >= size or col2 >= size:
                print("Invalid cell coordinates. Please try again.")
                continue

            if (row1, col1) in guessed_pairs or (row2, col2) in guessed_pairs:
                print("One or both of the selected cells have already been guessed. Please choose different cells.")
                continue
            
            if hidden_grid[row1][col1] == str(grid[row1][col1]) :
                hidden_grid_1[row1][col1] = True
            if hidden_grid[row2][col2] == str(grid[row2][col2]) :
                hidden_grid_1[row2][col2] = True

            hidden_grid[row1][col1] = str(grid[row1][col1])
            hidden_grid[row2][col2] = str(grid[row2][col2])
            print("option 1 display grid ")
            display_grid(hidden_grid)

            if grid[row1][col1] == grid[row2][col2]:
                print("Congratulations! You found a pair.")
                guessed_pairs.add((row1, col1))
                guessed_pairs.add((row2, col2))
                print("option 1 display grid after if condition ")
                display_grid(hidden_grid)

            else:
                print("Oops! The pair does not match.")
                hidden_grid[row1][col1] = 'X' if hidden_grid_1[row1][col1] != True else hidden_grid[row1][col1]

                hidden_grid[row2][col2] = 'X' if hidden_grid_1[row2][col2] != True else hidden_grid[row2][col2]

            attempts += 1

            # Pause for 2 seconds before hiding the numbers again
            time.sleep(2)
            system("clear")
            

        elif option == '2':
            print("Enter the coordinates of the cell to uncover (e.g., A0):")
            print("your attempt is", attempts)
            cell = input()

            row, col = get_coordinates(cell)

            if row >= size or col >= size:
                print("Invalid cell coordinates. Please try again.")
                continue

            if (row, col) in guessed_pairs:
                print("The selected cell has already been guessed. Please choose a different cell.")
                continue

            hidden_grid[row][col] = str(grid[row][col])
            print("option 2 display grid ")
            display_grid(hidden_grid)

            # Pause for 2 seconds before hiding the number again
            time.sleep(2)
            #hidden_grid[row][col] = 'X'

            
            system("clear")
            #print("attempts now ", attempts, size*size - 1)
            if attempts == size*size - 1 :
                print("You cheated - Loser! Your score is 0!")
                attempts=0
                break
            attempts += 1


        elif option == '3':
            print("option 3 display grid ")
            display_grid(grid)
            print("You gave up! Better luck next time.")
            break
 
        elif option == '4':
            print("Starting a new game...")
            play_game(size)
            return

        elif option == '5':
            print("Thanks for playing!")
            sys.exit()

        else:
            print("Invalid option. Please choose a valid option.")
            continue

        # Check if all pairs have been found
        if len(guessed_pairs) == size * size // 2:
            display_grid(grid)
            print("Congratulations! You found all the pairs.")
            break

    # Calculate the score
    if option != '3' and attempts > 0:
        min_guesses = size * size // 2
        score = (min_guesses / (attempts + 1)) * 100
        print("your number of guesses were ------- ", min_guesses)
        print ("total attempts ------", attempts+1)
        print(f"Your score is: {score:.1f}")



def main():
    if len(sys.argv) < 2:
        print("Please provide the grid size as a command-line argument.")
        return

    grid_size = int(sys.argv[1])
    if grid_size not in [2, 4, 6]:
        print("Invalid grid size. Please choose from 2, 4, or 6.")
        return

    play_game(grid_size)

if __name__ == "__main__":
    main()
