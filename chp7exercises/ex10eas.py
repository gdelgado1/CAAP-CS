# # A formula for computing Easter in the years 1982-2048
def yearinterval(year):
	if 1900 <= year <= 2099:
		return 'valid'
	else:
		return 'invalid'

def main():
	print("This program prints out Easter's date that year")
	year = eval(input("What is the year (1900 - 2099)? "))
	if year == 1954 or year == 2049 or year == 1981 or year == 2076: 
		a = year%19
		b = year%4
		c = year%7
		d = (19 * a + 24)%30
		e = (2 * b + 4 * c + 6 * d + 5)%7
		day = 22 + d + e
		day = day - 7
		if day > 31:
			day = day - 31
			print("Easter in {0} is April {1}.".format(year, day))
		else:
			print("Easter in {0} is March {1}.".format(year, day))
	elif yearinterval(year) == 'valid':
		a = year%19
		b = year%4
		c = year%7
		d = (19 * a + 24)%30
		e = (2 * b + 4 * c + 6 * d + 5)%7
		day = 22 + d + e
		if day > 31:
			day = day - 31
			print("Easter in {0} is April {1}.".format(year, day))
		else:
			print("Easter in {0} is March {1}.".format(year, day))
	else:
		print("Invalid Year.")
  
main()