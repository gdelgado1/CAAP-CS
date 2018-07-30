# takes the number of rows and columns and makes a matrix of those dimensions
# Jesus helped me! 
def make_matrix(row, col):
	matrix = []
	for i in range(row):
		mylist = []
		for j in range(col):
			mylist.append(0)
		matrix.append(mylist)
	return matrix

# takes two matrices and multiplies them returning the resulting matrix
def matrixmult(ar,bo):
	if len(ar[0]) == len(bo):
		product = multi_matrix(len(ar), len(bo[0]))
		for i in range(len(product)): 
			for j in range(len(product[0])): 
				temp_var = 0
				for z in range(len(bo)):
					product[i][j] += float(ar[z][n]) * float(bo[z][j])
		return product
	else:
		return []

# prints the given matrix, mostly for testing purposes
def print_matrix(m):
	for i in range(len(m)):
		print(m[i])

# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation(in_matrix, tran_matrix, sim_num):
	val = 0
	for i in range(sim_num):
		loop = True
		moves = 0
		temp_matrix = matrixmult(in_matrix, tran_matrix)
		while loop == True:
			temp_matrix = matrixmult(temp_matrix, tran_matrix)
			moves += 1
			print(str(moves) + " >> " + str(temp_matrix))
			if float(temp_matrix[0][11]) > float(0.99):
				val += moves
				loop = False
				print('end loop')
	return float(val)/sim_num