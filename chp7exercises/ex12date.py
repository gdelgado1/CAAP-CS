#Note this program only outputs the year if less than or equal to 2018  
#This program accepts a date in the form month date year and outputs whether or not the date is valid. 
import datetime 
def datevalidator():
	print ("This program accepts dates in the following form: mm/dd/yyyy and outputs whether or not they are true only if <= 2018. ")
	dat = str (input ("What is the date (Please remember to use / for separation)? ")) 
	newdat = dat.split("/")
	month = int(newdat[0])
	day = int(newdat[1])
	year = int(newdat[2])
	if year <= 2018:
		if month == 1 or month == 3 or month == 5 or month == 8 or month == 10 or month == 12: 
			if day <= 31: 
				print ("True") 
			else: 
				print ("This is not a valid date!")
		elif month == 4 or month == 6 or month == 9 or month == 11: 
			if day <=  30:
				print  ("True") 
			else: 
				print ("This is not a valid date!")
	else:
		print ("This is not a valid date as it has not yet happened!")
datevalidator()