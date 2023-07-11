#main file project

import chess
import pygame
import time
import sys

# ---------------------------------------creating pieces class ----------------------

class Piece:
	def __init__(self, type, image, killable=False):
		self.type = type
		self.killable = killable
		self.image = image

bp = Piece('P', 'Pieces_png/pb.png')
wp = Piece('p', 'Pieces_png/pw.png')
bk = Piece('K', 'Pieces_png/kb.png')
wk = Piece('k', 'Pieces_png/kw.png')
br = Piece('R', 'Pieces_png/rb.png')
wr = Piece('r', 'Pieces_png/rw.png')
bb = Piece('B', 'Pieces_png/fb.png')
wb = Piece('b', 'Pieces_png/fw.png')
bq = Piece('Q', 'Pieces_png/qb.png')
wq = Piece('q', 'Pieces_png/qw.png')
bc = Piece('C', 'Pieces_png/cb.png')
wc = Piece('c', 'Pieces_png/cw.png')

starting_order = {(0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bc.image),
				  (2, 0): pygame.image.load(bb.image), (3, 0): pygame.image.load(bk.image),
				  (4, 0): pygame.image.load(bq.image), (5, 0): pygame.image.load(bb.image),
				  (6, 0): pygame.image.load(bc.image), (7, 0): pygame.image.load(br.image),
				  (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
				  (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
				  (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
				  (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

				  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
				  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
				  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
				  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
				  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
				  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
				  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
				  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

				  (0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
				  (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
				  (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
				  (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
				  (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wc.image),
				  (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wk.image),
				  (4, 7): pygame.image.load(wq.image), (5, 7): pygame.image.load(wb.image),
				  (6, 7): pygame.image.load(wc.image), (7, 7): pygame.image.load(wr.image),}


# ------------------------Fonction to print grid---------------------------------------------

def print_grid(WIDTH, WHITE, WIN):
	i = 0
	while i < 8:
		j = 0
		while j < 8:
			pygame.draw.rect(WIN, WHITE, pygame.Rect(j * (WIDTH / 8), i * (WIDTH / 8), WIDTH / 8, WIDTH / 8))
			j += 2
		i += 1
		j = 1
		while j < 8:
			pygame.draw.rect(WIN, WHITE, pygame.Rect(j * (WIDTH / 8), i * (WIDTH / 8), WIDTH / 8, WIDTH / 8))
			j += 2
		i += 1
	pygame.display.flip()


# -----------------------Init window and looping it------------------------------------------


WIDTH = 800
done = False
WHITE = (250,235,215)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))
keys=pygame.key.get_pressed()
pygame.display.set_caption("Chess")
print_grid(WIDTH, WHITE, WIN)

while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			keys = pygame.key.get_pressed()
	
	if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
		done = True

pygame.quit()

#--------------------------------checking mat and pat---------------------------------------


# board = chess.Board()
# board = chess.Board("k7/8/8/8/8/8/5q2/7K")													 #stalemate situation
# board = chess.Board("k7/8/8/8/8/8/8/7K")														 #pat no check mate possible
# board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")      #check mate



# while (1)
# 	if (board.is_stalemate() == True):
# 		print("Pat by stalemate")
# 		break
# 	if (board.is_insufficient_material() == True):
# 		print("Pat : no way to end the game by check mate")
# 		break
# 	if (board.is_checkmate() == True):
# 		print("Check mate")
# 		break
