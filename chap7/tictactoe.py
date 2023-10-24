import random

board = [" " for _ in range(9)]

print("  Welcom to the greatest intellectual challenge of all time: Tic-Tac-Toe.")
print("  This will be a show down between your human brain and my silicon processor.\n\n")
print("  You will make your move known by entering a number, 0 - 8. The number will correspond to the board position as illustrated:")
print("         0 | 1 | 2")
print("         ---------")
print("         3 | 4 | 5")
print("         ---------")
print("         6 | 7 | 8")
print("  Prepare yourself, human. The ultimate battle is about to begin.\n\n")

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
def choose_symbol():
    while True:
        symbl = input("Do you require the first? <y/n>").lower()
        if symbl == "y":
          return "X"
        elif symbl == "n":
          return "O"
        else:
            print("Invalid choice. Please select y or n")


def user_move(board, symbol):
    while True:
        try:
            move = int(input("Where will you move? (0 - 8): "))
            if move >= 0 and move < 9 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")

def computer_move(board, symbol, user_moves):
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    if 0 in user_moves and 1 in user_moves:
        if 2 in empty_cells:
            return 2
    if 0 in user_moves and 2 in user_moves:
        if 1 in empty_cells:
            return 1
    if 1 in user_moves and 2 in user_moves:

        if 0 in empty_cells:
            return 0
    if 0 in user_moves and 3 in user_moves:
        if 6 in empty_cells:
            return 6
    if 0 in user_moves and 6 in user_moves:
        if 3 in empty_cells:
            return 3
    if 3 in user_moves and 6 in user_moves:
        if 0 in empty_cells:
            return 0
    if 3 in user_moves and 4 in user_moves:
        if 5 in empty_cells:
            return 5
    if 3 in user_moves and 5 in user_moves:
        if 4 in empty_cells:
            return 4
    if 4 in user_moves and 5 in user_moves:
        if 3 in empty_cells:
            return 3
    if 6 in user_moves and 7 in user_moves:
        if 8 in empty_cells:
            return 8
    if 6 in user_moves and 8 in user_moves:
        if 7 in empty_cells:
            return 7
    if 7 in user_moves and 8 in user_moves:
        if 6 in empty_cells:
            return 6
    if 1 in user_moves and 4 in user_moves:
        if 7 in empty_cells:
            return 7
    if 1 in user_moves and 7 in user_moves:
        if 4 in empty_cells:
            return 4
    if 4 in user_moves and 7 in user_moves:

        if 1 in empty_cells:
            return 1
    if 2 in user_moves and 5 in user_moves:
        if 8 in empty_cells:
            return 8
    if 5 in user_moves and 8 in user_moves:
        if 2 in empty_cells:
            return 2
    if 2 in user_moves and 8 in user_moves:
        if 5 in empty_cells:
            return 5
    if 0 in user_moves and 4 in user_moves:
        if 8 in empty_cells:
            return 8
    if 0 in user_moves and 8 in user_moves:
        if 4 in empty_cells:
            return 4
    if 4 in user_moves and 8 in user_moves:
        if 0 in empty_cells:
            return 0
    if 2 in user_moves and 4 in user_moves:
        if 6 in empty_cells:
            return 6
    if 2 in user_moves and 6 in user_moves:
        if 4 in empty_cells:
            return 4
    if 4 in user_moves and 6 in user_moves:
        if 2 in empty_cells:
            return 2
    return random.choice(empty_cells)


def is_game_over(board):
    for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]:
        if board[a] == board[b] == board[c] == "X":
            return "User wins"
        elif board[a] == board[b] == board[c] == "O":
            return "Computer wins"
    if " " not in board:
        return "It's a tie"
    return False
  
def play_game():
    symbol = choose_symbol()
    computer_symbol = "O" if symbol == "X" else "X"

    while True:
        user_moves = [] 

        print_board(board)

        if is_game_over(board) == "User wins":
            print("X win! \nNo, no! it cannot be! Somehow you tricked me, human.\nBut never again! I, the computer, so swears it!")
            break
        elif is_game_over(board) == "Computer wins":
            print("O won!.\nAs i predicted, human, i am triumphant once more.\nProop that computers are superior to humans in all regards.")
            break
        elif is_game_over(board) == "It's a tie":
            print("It's a tie! The game is a draw.")
            break

        if symbol == "X":
            move = user_move(board, symbol)
        else:
            move = computer_move(board, computer_symbol, user_moves)

        board[move] = symbol
        user_moves.append(move)

        if is_game_over(board) == "User wins":
            print_board(board)
            print("You win! Congratulations!")
            break

        print_board(board)
        if symbol == "O":
            move = user_move(board, symbol)
        else:
            move = computer_move(board, computer_symbol, user_moves)

        board[move] = computer_symbol

if __name__ == "__main__":
    play_game()
