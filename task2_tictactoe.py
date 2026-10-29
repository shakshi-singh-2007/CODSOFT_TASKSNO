# Task 2: Tic-Tac-Toe AI using Minimax with Alpha-Beta Pruning
# Human plays X, AI plays O. The AI never loses (best case for the human is a draw).

import math

WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
             (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
             (0, 4, 8), (2, 4, 6)]              # diagonals

def print_board(b):
    print()
    for r in range(3):
        print(" " + " | ".join(b[r * 3:r * 3 + 3]))
        if r < 2:
            print("---+---+---")
    print()

def winner(b):
    for a, c, d in WIN_LINES:
        if b[a] == b[c] == b[d] != " ":
            return b[a]
    return None

def is_full(b):
    return " " not in b

def minimax(b, is_ai_turn, alpha, beta):
    w = winner(b)
    if w == "O":
        return 1        # AI wins
    if w == "X":
        return -1       # human wins
    if is_full(b):
        return 0        # draw

    if is_ai_turn:      # AI tries to maximize the score
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False, alpha, beta))
                b[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha:   # alpha-beta pruning
                    break
        return best
    else:               # human tries to minimize the score
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True, alpha, beta))
                b[i] = " "
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def best_move(b):
    best_score, move = -math.inf, None
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax(b, False, -math.inf, math.inf)
            b[i] = " "
            if score > best_score:
                best_score, move = score, i
    return move

def main():
    board = [" "] * 9
    print("Tic-Tac-Toe: You are X, the AI is O.")
    print("Positions:\n 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")
    while True:
        print_board(board)
        try:
            pos = int(input("Your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        if pos not in range(9) or board[pos] != " ":
            print("Invalid or occupied position. Try again.")
            continue
        board[pos] = "X"
        if winner(board) or is_full(board):
            break
        board[best_move(board)] = "O"
        if winner(board) or is_full(board):
            break
    print_board(board)
    w = winner(board)
    print("You win!" if w == "X" else "The AI wins!" if w == "O" else "It's a draw!")

if __name__ == "__main__":
    main()
