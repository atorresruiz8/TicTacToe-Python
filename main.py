# TicTacToe Game
# Global Variables

# Game board
board = ["-", "-", "-",
"-", "-", "-",
"-", "-", "-",]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Who's turn is it 
current_player = "X"

# Display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn(player):
  # print the current player
  print(player + "'s turn.")

  # take in user input
  position = input("Choose a position from 1-9: ")

  # used to loop for checking valid movements
  valid = False

  # Check to see if the player is making valid moves (not putting a character on a filled spot in the board)
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid input. Choose a position from 1 to 9: ")

    # convert position string into int for indexing board array
    # subtract 1 because array indices start at 0
    position = int(position) - 1

    # check to see if the position on the board is empty
    if board[position] == "-":
      valid = True
    else:
      print("That spot is filled. Try another.")

  # place your piece at the input position
  board[position] = player

  # display the current board
  display_board()

# Checks to see if there are 3 of the same characters in a row
def check_rows():
  # setup global Variables
  global game_still_going

  # check if any of the rows have all the same value and are not "-"
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  # If any row does have a match, flag that there is a win and stop the game
  if row_1 or row_2 or row_3:
    game_still_going = False
  
  # return the player in the first square of the row because all the players in a row are the same
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

# Checks to see if there are 3 of the same characters in a column
def check_columns():
  # setup global Variables
  global game_still_going

  # check if any of the columns have all the same value and are not "-"
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"

  # If any column does have a match, flag that there is a win and stop the game
  if col_1 or col_2 or col_3:
    game_still_going = False
  
  # return the player in the first square of the column because all the players in a column are the same
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return

# Checks to see if there are 3 of the same characters in a diagonal
def check_diagonals():
  # setup global Variables
  global game_still_going

  # check if any of the diagonal have all the same value and are not "-"
  diag_1 = board[0] == board[4] == board[8] != "-"
  diag_2 = board[6] == board[4] == board[2] != "-"

  # If any diagonal does have a match, flag that there is a win and stop the game
  if diag_1 or diag_2:
    game_still_going = False
  
  # return the player in the first square of the diagonal because all the players in a diagonal are the same
  if diag_1:
    return board[0]
  elif diag_2:
    return board[6]
  return

# Check to see if any player won
def check_if_win():
  # set the global variable winner
  global winner

  #check rows
  row_winner = check_rows()
  #check columns
  col_winner = check_columns()
  #check diagonals
  diag_winner = check_diagonals()
  
  if row_winner:
    winner = row_winner
  elif col_winner:
    winner = col_winner
  elif diag_winner:
    winner = diag_winner
  else:
    winner = None
  return

# Check to see if neither player won
def check_if_tie():
  # setup global Variables
  global game_still_going

  # if there are no longer any "-" in the board, then the board is filled
  # no more inputs could happen and the game ended in a tie
  if "-" not in board:
    game_still_going = False
  return

# Check to see if a win condition is met
def check_if_game_over():
  check_if_win()
  check_if_tie()

# Swap between the players
def flip_player():
  # setup global Variables
  global current_player

  # if the current player was X, then change it to O
  if current_player == "X":
    current_player = "O"

  # if the current player was O, then change it to X
  elif current_player == "O":
    current_player = "X"
  return

# Play a game of TicTacToe
def play_game():
  # display initial board
  display_board()
  
  # loop through turns until the game is over
  while game_still_going:
    # handle a turn for the current player
    handle_turn(current_player)

    # check if any win conditions are met
    check_if_game_over()

    # swap to the next player
    flip_player()

  # the game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

# call the function to start the game
play_game()