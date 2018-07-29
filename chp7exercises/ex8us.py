def usgov():
	print ("This program determines whether or not you can become a US Senator or US Representative.")
	age=int(input("How old are you? "))
	citi=eval(input("How long have you been a citizen of the United States? "))
	if age >= 30 and citi >= 9: 
		print ("You qualify to become a United States Senator.")
	elif age>= 25 and citi >= 7: 
		print ("You qualify to become a United States Respresentative.")
	else: 
		print ("You do not qualify for either position.")

usgov()