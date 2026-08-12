

board = [" " for i in range(9)]


# Display board
def display_board():

    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Check winner
def check_winner(player):

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# Check draw
def check_draw():

    return " " not in board


# Main game
current_player = "X"

while True:

    display_board()

    print("Player", current_player)

    position = int(input("Enter position (1-9): "))

    position = position - 1

    # Check position
    if position < 0 or position > 8:
        print("Invalid position!")
        continue

    if board[position] != " ":
        print("Position already taken!")
        continue

    # Place X or O
    board[position] = current_player

    # Check winner
    if check_winner(current_player):

        display_board()

        print("🎉 Player", current_player, "wins!")
        break

    # Check draw
    if check_draw():

        display_board()

        print("It's a draw!")
        break

    # Change player
    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"
