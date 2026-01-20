import numpy as np
import pygame
import math
import sys
import os

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

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

def draw_board(board):
  #Draw board in pygame
  for c in range(COLUMN_COUNTS):
    for r in range(ROW_COUNTS):
      pygame.draw.rect(screen, BLUE, (c * SQUARSIZE, r * SQUARSIZE + SQUARSIZE, SQUARSIZE, SQUARSIZE))
      pygame.draw.circle(screen, BLACK, (int(c * SQUARSIZE + SQUARSIZE / 2), int(r*SQUARSIZE + SQUARSIZE + SQUARSIZE / 2)), RADIUS)
  
  for c in range(COLUMN_COUNTS):
    for r in range(ROW_COUNTS):
      if board[r][c] == 1:
        pygame.draw.circle(screen, RED, (int(c * SQUARSIZE + SQUARSIZE / 2), height-int(r*SQUARSIZE + SQUARSIZE / 2)), RADIUS)
      elif board[r][c] == 2:
        pygame.draw.circle(screen, YELLOW, (int(c * SQUARSIZE + SQUARSIZE / 2), height-int(r*SQUARSIZE + SQUARSIZE / 2)), RADIUS)
  
  pygame.display.update()


board = creat_board()
game_over = False
turn = 0

pygame.init()

SQUARSIZE = 100 

width = COLUMN_COUNTS * SQUARSIZE
height = (ROW_COUNTS + 1) * SQUARSIZE

size = (width, height)

RADIUS = int(SQUARSIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

#Main game logic
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.MOUSEMOTION:
      pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARSIZE))
      posx = event.pos[0]
      if turn % 2 == 0:
        pygame.draw.circle(screen, RED, (posx, int(SQUARSIZE/2)), RADIUS)
      else:
        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARSIZE/2)), RADIUS)
    
    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
      pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARSIZE))

      # Ask for Player 1 Input
      if turn % 2 == 0:
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARSIZE))

        if is_valid_location(board, col):
          row = get_next_open_row(board, col)
          drop_piece(board, row, col, 1)

          if winning_move(board, 1):
            label = myfont.render("PLAYER 1 Wins!!!", 1, RED)
            screen.blit(label, (40,10))
            game_over = True

      # Ask for Player 2 Input
      else:
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARSIZE))

        if is_valid_location(board, col):
          row = get_next_open_row(board, col)
          drop_piece(board, row, col, 2)

        if winning_move(board, 2):
            label = myfont.render("PLAYER 2 Wins!!!", 1, YELLOW)
            screen.blit(label, (40,10))
            game_over = True

      draw_board(board)
      turn += 1

      if game_over:
        pygame.time.wait(3000)

