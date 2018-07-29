# exercise 2 from chapter 7.
# updating it using decisions and/or exception handling 
# Angel tested it! 
def quizscorer():
	print ("This program accepts a quiz score as an input and uses a decision structure to calculate the corresponding grade.")
	try:
		score=int(input("What is the score the student recieved on the exam? "))
		if score > 5: 
			print ("This is not an acceptable quiz score. No grade can be calculated.")
		elif score == 5:
			print ("The student's grade is A!")
		elif score == 4: 
			print ("The student's grade is B!")
		elif score == 3: 
			print ("The student's grade is C!")
		elif score == 2: 
			print ("The student's grade is D!")
		elif score <= 1: 
			print ("The student's grade is F!")
	except ValueError: 
		print ("Has to be a number!")
	input()
quizscorer()