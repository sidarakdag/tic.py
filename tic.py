"""
Tic Tac Toe - two players take turns on the same keyboard.
Run with: python tic_tac_toe.py
"""

def print_board(board):
    print()
    for i in range(3):
        row = board[i*3:i*3+3]
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return " " not in board


def get_move(player, board):
    while True:
        choice = input(f"Player {player}, enter a position (1-9): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Please enter a number from 1 to 9.")
            continue
        pos = int(choice) - 1
        if board[pos] != " ":
            print("That spot is taken. Try again.")
            continue
        return pos


def main():
    board = [" "] * 9
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9, left to right, top to bottom:")
    print_board([str(i + 1) for i in range(9)])

    while True:
        current = players[turn % 2]
        print_board(board)
        pos = get_move(current, board)
        board[pos] = current

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

    again = input("Play again? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
