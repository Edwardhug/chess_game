#main file project

import chess

# board = chess.Board()
# board = chess.Board("k7/8/8/8/8/8/5q2/7K")		#stalemate situation
# board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")

print(board)
if (board.is_stalemate() == True):		#Pat Checker with no move possible
	print("Pat by stalemate")
# if (board.outcome() == Outcome(termination=<Termination.CHECKMATE: 1>, winner=True)):
# 	print("Check mate")

board.outcome()
# Outcome(termination=<Termination.CHECKMATE: 1>, winner=True)