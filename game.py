def print_board(board):
    print('-------------')
    for row in board:
        print('|', end='')
        for col in row:
            print(' ' + col + ' |', end='')
        print('\n-------------')

def get_move(player):
    while True:
        move = input(f"Player {player}, enter a valid move (e.g. 1,2): ")
        if len(move) == 3 and move[1] == ',' and move[0].isdigit() and move[2].isdigit():
            row = int(move[0]) - 1
            col = int(move[2]) - 1
            if row >= 0 and row < 3 and col >= 0 and col < 3:
                return (row, col)
        print("Invalid move. Please try again.")

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':
            return row[0]
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != '-':
            return board[0][col]
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != '-':
        return board[0][0]
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != '-':
        return board[0][2]
    return None

def play_game():
    board = [['-' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        move = get_move(players[current_player])
        board[move[0]][move[1]] = players[current_player]
        winner = check_winner(board)
        if winner:
            print(f"Congratulations! Player {winner} wins!")
            return
        if all([col != '-' for row in board for col in row]):
            print("It's a tie!")
            return
        current_player = (current_player + 1) % 2

def play_again():
    while True:
        answer = input("Do you want to play again? (y/n): ")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

while True:
    play_game()
    if not play_again():
        break
