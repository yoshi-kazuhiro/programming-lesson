RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
END = '\033[0m'

print("□ □ □ ")
print("□ □ □ ")
print("□ □ □ ")

array = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

for i in range(0, 3):
	for j in range(0, 3):
		print(str(array[i][j]) + ", ", end="")
	print("")


board = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def print_board(): 
	for i in range(0, 3):
		for j in range(0, 3):
			if board[i][j] == 0:
				print("□ ", end="")
			elif board[i][j] == 1:
				print("〇 ", end="")
			elif board[i][j] == 2:
				print("× ", end="")
			else:
				print("？ ", end="")
		print("")

def print_board_index(): 
	print("  0 1 2 -j")
	for i in range(0, 3):
		print(str(i) + " ", end="")
		for j in range(0, 3):
			if board[i][j] == 0:
				print("□ ", end="")
			elif board[i][j] == 1:
				print(RED, end="")
				print("O ", end="")
				print(END, end="")
			elif board[i][j] == 2:
				print(BLUE, end="")
				print("X ", end="")
				print(END, end="")
			else:
				print(GREEN, end="")
				print("？ ", end="")
				print(END, end="")
		print("")
	print("|")
	print("i")


def check_input(i, j, v):
	try: 
		I = int(i)
		J = int(j)
		V = int(v)
		if I >= 0 and I < 3:
			#print("i OK")
			pass
		else: 
			print("iは0～2を入力してください！スキップ！")
			return

		if J >= 0 and J < 3:
			##print("j OK")
			pass
		else: 
			print("jは0～2を入力してください！スキップ！")
			return

		if board[I][J] != 0:
			print("すでに置かれています！スキップ！")
		else:
			board[I][J] = V
	except:
		print("間違った入力です！スキップ！")

def check_game():
	if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or \
		(board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1) or \
		(board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or \
		(board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or \
		(board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or \
		(board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or \
		(board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or \
		(board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1): 
			print(RED)
			print("===先行の勝ち！===")
			print(END)
			return
	if (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2) or \
		(board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2) or \
		(board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2) or \
		(board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2) or \
		(board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2) or \
		(board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2) or \
		(board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2) or \
		(board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2): 
			print(BLUE)
			print("===後攻の勝ち！===")
			print(END)
			return


print("ゲームスタート！")
print_board_index()


while True:
	print(RED)
	print("先攻の番です")
	print(END)
	i = input("i: ")
	j = input("j: ")
	#print("i: " + str(i) + ", j: " +str(j))
	#board[int(i)][int(j)] = 1
	check_input(i, j, 1)
	print_board_index()
	check_game()
	print(BLUE)
	print("後攻の番です")
	print(END)
	i = input("i: ")
	j = input("j: ")
	#print("i: " + str(i) + ", j: " +str(j))
	#board[int(i)][int(j)] = 2
	check_input(i, j, 2)
	print_board_index()
	check_game()
