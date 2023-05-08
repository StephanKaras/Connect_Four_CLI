# Connect 4 Game Documentation

## Introduction
Connect 4 is a classic board game that is played by two players. The objective of the game is to connect four of your pieces vertically, horizontally, or diagonally before your opponent does.

This Python program allows you to play the game against another player or against the computer. The computer uses the minimax algorithm to choose the best move.

## Author
**Stephan Karas** - This program was created by Stephan Karas on 25.04.2023.

## Requirements
This program requires Python 3 to be installed on your machine.

## Getting Started
1. Download the "Connect_four" program from the repository.
2. Open the command line and navigate to the directory where the program is saved.
3. Run the program using the following command: `python connect_four.py`.

## How to Play
1. When prompted, enter the number of the game mode you would like to play:
    - **1:** Play against another player
    - **2:** Play against the computer using the minimax algorithm
2. If you chose to play against another player, you will take turns dropping your pieces into the board by selecting a column to drop the piece into.
3. If you chose to play against the computer, you will be the first to drop a piece. The computer will then choose the best move using the minimax algorithm and drop its piece. The game will continue in this way until one player wins or the board is full.
4. To drop a piece into a column, enter the number of the column you would like to drop your piece into.
5. The game will continue until one player wins or the board is full.
6. If you would like to quit the game, enter "q" when prompted for a column number.
7. If you would like to restart the game, enter "r" when prompted for a column number.

## Code Explanation
The program consists of a single Python file called `connect_four.py`. Here is an overview of the code:

### Constants
- `ROWS`: The number of rows on the game board
- `COLUMNS`: The number of columns on the game board
- `GAME_OVER`: A boolean value that indicates whether the game is over

### Board Class
The `board` class represents the game board. It has the following methods:

#### Constructor
- `__init__(self, rows, cols)`: Creates a 2D list to represent the game board with the specified number of rows and columns.

#### Display Board
- `display(self)`: Prints the current state of the game board.

#### Add Piece
- `add_piece(self, piece)`: Prompts the user to enter a column number and drops a piece into the specified column.

#### Add Computer Piece
- `add_computer_piece(self, piece)`: Chooses a random column and drops a piece into the specified column.

#### Check for Win
- `has_won(self, piece)`: Checks if the specified player has won the game.

### Play Against Another Player
- `play_against_player()`: Starts a new game where two human players can play against each other.

### Play Against the Computer
- `play_against_computer()`: Starts a new game where the user can play against the computer.

## Conclusion
This program allows you to play Connect 4 against another player or against the computer. The computer uses the minimax algorithm to choose the best move.
