#main file project

import chess

board = chess.Board()
# board = chess.Board("k7/8/8/8/8/8/5q2/7K")													 #stalemate situation
# board = chess.Board("k7/8/8/8/8/8/8/7K")														 #pat no check mate possible
# board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")      #check mate

print(board)
if (board.is_stalemate() == True):
	print("Pat by stalemate")
if (board.is_insufficient_material() == True):
	print("Pat : no way to end the game by check mate")
if (board.is_checkmate() == True):
	print("Check mate")