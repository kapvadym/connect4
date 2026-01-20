import numpy as np
import os

ROW_COUNTS = 6
COLUMN_COUNTS = 7

def creat_board():
  board = np.zeros((ROW_COUNTS, COLUMN_COUNTS))
  return board

def drop_piece(board, row, col, piece):
  board[row][col] = piece

def is_valid_location(board, col):
  return board[ROW_COUNTS - 1][col] == 0

def get_next_open_row(board, col):
  for r in range(ROW_COUNTS):
    if board[r][col] == 0:
      return r 

def print_board(board):
  print(np.flip(board, 0))

board = creat_board()
game_over = False
turn = 0

while not game_over:
  os.system('cls' if os.name == 'nt' else 'clear')
  print_board(board)
  
  # Ask for Player 1 Input
  if turn % 2 == 0:
    col = int(input("Player 1 Make your Selection (0-6):"))

    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 1)

  # Ask for Player 2 Input
  else:
    col = int(input("Player 2 Make your Selection (0-6):"))

    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 2)

  turn += 1

