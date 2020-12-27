# ----Game Board ----

#  --Global variable--

# if game still going
game_still_going = True

# win or tie
winner = None
# who's turn is it ?
current_player = "X"

board =["-","-","-",
        "-","-","-",
        "-","-","-"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display initial board
    display_board()
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()
    # flip other player
        flip_player()
    # the game has ended
    if winner == "X" or winner == "O":
         print(winner," won.")
    elif winner == None:
        print("Tie")


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    # check row
    row_winner = check_rows()
    # check column
    column_winner = check_columns()
    # check diagonal
    diagonal_winner  = check_diagonals()
    if row_winner:
        # there is a winner
        winner = row_winner
    elif column_winner:
        # there is a winner
        winner = column_winner
    elif diagonal_winner:
        # there is a winner
        winner = diagonal_winner
    else:
        #there is no win
        winner = None
    return


def check_rows():
    # setup global variable
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[4] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # end the game if any row is True
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # setup global variable
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # end the game if any row is True
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # setup global variable
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
        # end the game if any row is True
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    # setup global
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # setup global
    global current_player
    if current_player =="X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


def handle_turn(player):
    print(player,"'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) -1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()


play_game()