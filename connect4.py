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

def winning_move(board, piece):
  #Check horizontal location for win
  for c in range(COLUMN_COUNTS - 3):
    for r in range(ROW_COUNTS):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        return True

  #Check verical location for win
  for c in range(COLUMN_COUNTS):
    for r in range(ROW_COUNTS - 3):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True

  #Check positive sloped diagonal
  for c in range(COLUMN_COUNTS - 3):
    for r in range(ROW_COUNTS - 3):
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        return True

  #Check negative sloped diagonal
  for c in range(COLUMN_COUNTS - 3):
    for r in range(3, ROW_COUNTS):
      if board[r][c] == piece and board[r-1][c-1] == piece and board[r-2][c-2] == piece and board[r-3][c-3] == piece:
        return True


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

      if winning_move(board, 1):
        print("PLAYER 1 Wins!!!")
        game_over = True

  # Ask for Player 2 Input
  else:
    col = int(input("Player 2 Make your Selection (0-6):"))

    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 2)

    if winning_move(board, 2):
        print("PLAYER 2 Wins!!!")
        game_over = True

  turn += 1

