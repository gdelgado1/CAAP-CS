def speedlimit(): 
	print ("This program calculates your speeding ticket in Podunksville.")
	limit = eval(input("What was the speed limit? "))
	speed = eval(input("What was your speed? "))
	res = speed - limit 
	if res > 90: 
		fine = (res * 5) + 250
		print ("Your fine is $",fine,".") 
	else: 
		fine = (res* 5) + 50 
		print ("Your fine is $",fine,".")

speedlimit()