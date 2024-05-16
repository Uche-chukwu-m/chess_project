import chess

# Create a new chess board
board = chess.Board()

# Print the initial board state
print(board)

# Make a few moves
board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")

# Print the board after making moves
print(board)

# Get legal moves for the current position
legal_moves = list(board.legal_moves)
print("Legal moves:", legal_moves)