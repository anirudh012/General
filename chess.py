import random

def chess():

	r1 = 0
	sample_board = ['#','01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
	p1_board = ['#','E1.1','H1.1','P1.1','Q1.1','K1.1','P1.2','H1.2','E1.2','S1.1','S1.2','S1.3','S1.4','S1.5','S1.6','S1.7','S1.8']
	p2_board = ['#','S2.1','S2.2','S2.3','S2.4','S2.5','S2.6','S2.7','S2.8','E2.1','H2.1','P2.1','K2.1','Q2.2','P2.2','H2.2','E2.2']
	my_board = [['#',p1_board[1],p1_board[2],p1_board[3],p1_board[4],p1_board[5],p1_board[6],p1_board[7],p1_board[8]],[p1_board[9],p1_board[10],p1_board[11],p1_board[12],p1_board[13],p1_board[14],p1_board[15],p1_board[16]],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],[p2_board[1],p2_board[2],p2_board[3],p2_board[4],p2_board[5],p2_board[6],p2_board[7],p2_board[8]],[p2_board[9],p2_board[10],p2_board[11],p2_board[12],p2_board[13],p2_board[14],p2_board[15],p2_board[16]]]

	king = [1,7,8]
	queen = []
	soldier = [1,2]
	elephant = []
	pony = [9,18,27,36]



	def s_board():

		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[57]) + " | " + str(sample_board[58]) + " | " + str(sample_board[59]) + " | " + str(sample_board[60]) + " | " + str(sample_board[61]) + " | " + str(sample_board[62]) + " | " + str(sample_board[63]) + " | " + str(sample_board[64]) + " | ")
		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[49]) + " | " + str(sample_board[50]) + " | " + str(sample_board[51]) + " | " + str(sample_board[52]) + " | " + str(sample_board[53]) + " | " + str(sample_board[54]) + " | " + str(sample_board[55]) + " | " + str(sample_board[56]) + " | ")
		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[41]) + " | " + str(sample_board[42]) + " | " + str(sample_board[43]) + " | " + str(sample_board[44]) + " | " + str(sample_board[45]) + " | " + str(sample_board[46]) + " | " + str(sample_board[47]) + " | " + str(sample_board[48]) + " | ")
		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[33]) + " | " + str(sample_board[34]) + " | " + str(sample_board[35]) + " | " + str(sample_board[36]) + " | " + str(sample_board[37]) + " | " + str(sample_board[38]) + " | " + str(sample_board[39]) + " | " + str(sample_board[40]) + " | ")
		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[25]) + " | " + str(sample_board[26]) + " | " + str(sample_board[27]) + " | " + str(sample_board[28]) + " | " + str(sample_board[29]) + " | " + str(sample_board[30]) + " | " + str(sample_board[31]) + " | " + str(sample_board[32]) + " | ")
		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[17]) + " | " + str(sample_board[18]) + " | " + str(sample_board[19]) + " | " + str(sample_board[20]) + " | " + str(sample_board[21]) + " | " + str(sample_board[22]) + " | " + str(sample_board[23]) + " | " + str(sample_board[24]) + " | ")
		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[9]) + " | " + str(sample_board[10]) + " | " + str(sample_board[11]) + " | " + str(sample_board[12]) + " | " + str(sample_board[13]) + " | " + str(sample_board[14]) + " | " + str(sample_board[15]) + " | " + str(sample_board[16]) + " | ")
		print(" ----------------------------------------- ")
		print(" | " + str(sample_board[1]) + " | " + str(sample_board[2]) + " | " + str(sample_board[3]) + " | " + str(sample_board[4]) + " | " + str(sample_board[5]) + " | " + str(sample_board[6]) + " | " + str(sample_board[7]) + " | " + str(sample_board[8]) + " | ")
		print(" ----------------------------------------- ")

	def m_board():

		print(" ----------------------------------------------------- ")
		print(" | " + my_board[8][1] + " | " + my_board[8][2] + " | " + my_board[8][3] + " | " + my_board[8][4] + " | " + my_board[8][5] + " | " + my_board[8][6] + " | " + my_board[8][7] + " | " + my_board[8][8] + " | ")
		print(" ----------------------------------------------------- ")
		print(" | " + my_board[7][1] + " | " + my_board[7][2] + " | " + my_board[7][3] + " | " + my_board[7][4] + " | " + my_board[7][5] + " | " + my_board[7][6] + " | " + my_board[7][7] + " | " + my_board[7][8] + " | ")
		print(" ----------------------------------------------------- ")
		print(" | " + my_board[6][1] + " | " + my_board[6][2] + " | " + my_board[6][3] + " | " + my_board[6][4] + " | " + my_board[6][5] + " | " + my_board[6][6] + " | " + my_board[6][7] + " | " + my_board[6][8] + " | ")
		print(" ----------------------------------------------------- ")
		print(" | " + my_board[5][1] + " | " + my_board[5][2] + " | " + my_board[5][3] + " | " + my_board[5][4] + " | " + my_board[5][5] + " | " + my_board[5][6] + " | " + my_board[5][7] + " | " + my_board[5][8] + " | ")
		print(" ----------------------------------------------------- ")
		print(" | " + my_board[4][1] + " | " + my_board[4][2] + " | " + my_board[4][3] + " | " + my_board[4][4] + " | " + my_board[4][5] + " | " + my_board[4][6] + " | " + my_board[4][7] + " | " + my_board[4][8] + " | ")
		print(" ----------------------------------------------------- ")
		print(" | " + my_board[3][1] + " | " + my_board[3][2] + " | " + my_board[3][3] + " | " + my_board[3][4] + " | " + my_board[3][5] + " | " + my_board[3][6] + " | " + my_board[3][7] + " | " + my_board[3][8] + " | ")
		print(" ----------------------------------------------------- ")
		print(" | " + my_board[2][1] + " | " + my_board[2][2] + " | " + my_board[2][3] + " | " + my_board[2][4] + " | " + my_board[2][5] + " | " + my_board[2][6] + " | " + my_board[2][7] + " | " + my_board[2][8] + " | ")
		print(" ----------------------------------------------------- ")
		print(" | " + my_board[1][1] + " | " + my_board[1][2] + " | " + my_board[1][3] + " | " + my_board[1][4] + " | " + my_board[1][5] + " | " + my_board[1][6] + " | " + my_board[1][7] + " | " + my_board[1][8] + " | ")
		print(" ----------------------------------------------------- ")

###############################################################################################

	def is_blank1():
		if my_board[pos1] == '' or my_board[pos1] in p2_board:
			return True
		else:
			return False

	def is_blank2():
		if my_board[pos2] == '' or my_board[pos2] in p1_board:
			return True
		else:
			return False
	
	def move1(char1,pos1):
		index_pos1 = my_board.index(char1)
		my_board[index_pos1] = '' 
		my_board[pos1] = char1
		m_board()

	def move2(char2,pos2):
		index_pos2 = my_board.index(char2)
		my_board[index_pos2] = ''
		my_board[pos2] = char2 
		m_board()

	def valid_moves1():
		while True:
			row1 = input()
			row1 = int(row1)
			pos1 = input()
			pos1 = int(pos1)
			if char1[0] == 'K':
				current_pos1 = my_board.index(char1)
				if abs(current_pos1 - pos1) != 1 or abs(current_pos1 - pos1) != 8 or abs(current_pos1 - pos1) != 7:
					print('Please enter valid position.')
					continue
				else:
					break

	def valid_moves2():
		while True:
			pos2 = input()
			pos2 = int(pos2)
			if char2[0] == 'K':
				current_pos2 = my_board.index(char2)
				if abs(current_pos2 - pos2) != 1 or abs(current_pos2 - pos2) != 8 or abs(current_pos2 - pos2) != 7:
					print('Please enter valid position.')
					continue
				else:
					break

###############################################################################################

	print("")
	print('Welcome to the game of chess!')
	print("")
	print('Here is how you can choose the position on the board.')
	print("")
	s_board()

	print("Player 1: Please enter your name.")
	player1 = input()

	print("Player 2: Please enter your name.")
	player2 = input()

	print("Ready to play? (Y|N)")
	
	while True:
		game_on = input()
		game_on = game_on.upper()
		if game_on == "Y" or game_on == "N":
			break
		else:
			print('Please enter valid input. (Y|N)')

###############################################################################################

	while game_on == "Y":
		print('Lets start!')
		m_board()

		print(player1 + ', your turn. Please input the character you want to move and to which position.')
		while True:
			print('Please enter character.')
			char1 = input()
			if char1 in p1_board:
				break
			else:
				print('Please input valid character.')

		while True:
			print('Please enter board position.')
			valid_moves1()
			if is_blank1() == True:
				move1(char1,pos1)
				break
			else:
				print('This position is not empty.')

		if 'K2.1' not in my_board:
			print(player1 + ' wins!')
		
		#################################################
			

		print(player2 + ', your turn. Please input the character you want to move and to which position.')
		while True:
			print('Please enter character.')
			char2 = input()
			if char2 in p2_board:
				break
			else:
				print('Please input valid character.')

		while True:
			print('Please enter board position.')
			valid_moves2()
			if is_blank2() == True:
				move2(char2,pos2)
				break
			else:
				print('This position is not empty.')

		if 'K1.1' not in my_board:
			print(player2 + ' wins!')
			


		break



















chess()
