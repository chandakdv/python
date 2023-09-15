def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        
        move = get_move()
        row, col = (move - 1) // 3, (move - 1) % 3
        
        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("That cell is already occupied. Try again.")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = 'X' if player == 'O' else 'O'

if __name__ == "__main__":
    main()
