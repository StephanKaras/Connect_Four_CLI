'''
name: Connect 4
author: Stephan Karas
date: 25.04.2023
description: A simple Connect 4 game written in Python. The game can be played against another player or against the computer. The computer uses the minimax algorithm to choose the best move.
'''


import random


# constants
ROWS = 6
COLUMNS = 6
GAME_OVER = False

class board:

# constructor
    def __init__(self, rows, cols):
        self.rows = rows 
        self.cols = cols
        self.board = [[" " for j in range(cols)] for i in range(rows)] # create a 2D list of size rows x cols

# function to display the board
    def display(self):
        horizontal_line = "┌─" + "───┬─"*(self.cols-1) + "───┐"
        print(horizontal_line)
        for row in range(self.rows):
            print("│ ", end="")
            for col in range(self.cols):
                print(f"{self.board[row][col]}  │ ", end="")
            print()
            if row < self.rows - 1:
                print("├─" + "───┼─"*(self.cols-1) + "───┤")
        print("└─" + "───┴─"*(self.cols-1) + "───┘")
        print("  " + "    ".join(str(i+1) for i in range(self.cols)))

# function to add a piece to the board
    def add_piece(self, piece):
        while True: 
            col = input("Choose a column: ") # ask the first player to choose a column

            # if the input is q, quit the game. if the input is r, restart the game
            if col == "q":
                quit()
            elif col == "r":
                play_against_player()
            

            if col.isdigit() and int(col) in range(1, self.cols+1): # check if the input is valid 
                if self.board[0][int(col)-1] == " ": # check if the column is not full
                    break
                else:
                    print("Column is full, please try again")
            else:   
                print("Invalid input, please try again")
            

        col = int(col) - 1 # subtract 1 to make it zero-based
        
        for row in range(self.rows-1, -1, -1): # start from the bottom row and go up
            if self.board[row][col] == " ": # if the cell is empty
                self.board[row][col] = piece # add the piece to the cell
                break


    '''
    I was unfortunately not able to implement the minimax algorithm to make the computer choose the best move. 
    I tried to implement it but I was not able to get it to work in time. 
    I have included the code below instead to make the computer choose a random column, in order to make the game playable.
    '''
# function to add a piece to the board in a random column for the computer
    def add_computer_piece(self, piece):
        while True:
            col = random.randint(1, self.cols-1) # choose a random column
            if self.board[0][col] == " ": # check if the column is not full
                break
        
        for row in range(self.rows-1, -1, -1): # start from the bottom row and go up
            if self.board[row][col] == " ": # if the cell is empty
                self.board[row][col] = piece # add the piece to the cell
                break


   
# function to check if a player has won
    def has_won(self, piece):
        """Check if the player has won."""
        # check horizontal locations for win
        for c in range(self.cols-3):
            for r in range(self.rows):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        # check vertical locations for win 
        for c in range(self.cols):
            for r in range(self.rows-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        # check positively sloped diagonals
        for c in range(self.cols-3):
            for r in range(self.rows-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # check negatively sloped diagonals
        for c in range(self.cols-3):
            for r in range(3, self.rows):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

        return False
    

# function to play against another player
def play_against_player():
    board1 = board(ROWS, COLUMNS) # create a board object
    board1.display() # display the board

    while GAME_OVER == False:
        print("Player 1's turn") 
        board1.add_piece("X") # add the player's piece to the board
        board1.display() # display the board

        if board1.has_won("X") == True: # check if the player has won
            print("Player 1 has won!")
            break

        print("Player 2's turn") 
        board1.add_piece("O") # add the player's piece to the board
        board1.display() # display the board
        
        if board1.has_won("O") == True: # check if the player has won
            print("Player 2 has won!")
            break

# function to play against the computer
def play_against_computer():

    board2 = board(ROWS, COLUMNS) # create a board object
    board2.display() # display the board

    while GAME_OVER == False:
        print("Your turn") 
        board2.add_piece("X") # add the player's piece to the board
        board2.display() # display the board

        if board2.has_won("X") == True: # check if the player has won
            print("You have won!")
            break

        print("Computer's turn")
        board2.add_computer_piece("O") # add the AI's piece to the board
        board2.display() # display the board

        if board2.has_won("O") == True: # check if the computer has won
            print("Computer has won!")
            break

# main function of the game. the game starts by asking the player whether he wants to play against another player or against the computer. 
def main():
    print("\nWelcome to Connect 4!\n")
    print("Please choose an option:")
    print("1. Play against another player")
    print("2. Play against the computer")
    print("3. Exit\n")
    print("At any point you can enter q to quit the game or r to restart the game")

    
    choice = input("Enter your choice: ")
    if choice == "1":
        play_against_player() 
    elif choice == "2":
        play_against_computer()
    elif choice == "3":
        print("Goodbye!")
        exit()  # exit the program
    else:
        print("Invalid choice. Please try again.")
        main()

main()