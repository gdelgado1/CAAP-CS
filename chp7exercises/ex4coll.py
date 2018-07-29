def collegeassign():
	print ("This program classifies students according to credits earned.")
	credits=int(input("How many credits do you have thus far? "))
	if credits >= 26:
		print ("You are a senior!")
	elif credits >= 16: 
		print ("You are a junior!")
	elif credits >= 7: 
		print ("You are a sophomore!")
	elif credits < 7: 
		print ("You are a freshman!")

	input()
collegeassign()