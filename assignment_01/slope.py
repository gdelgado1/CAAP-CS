#A program to sum a series of number entered by the user. 
def sumslope(): 
    print ("This prorgam will give the sum of numbers provided by the user.")
    tot = 0
    many= int(input("How many numbers would you like to add up: "))
    for i in range(many): 
        digits= eval(input("Provide me with a digit from the list: "))
        tot=tot+digits
    print ("The sum of the given digits is",tot,".")  
sumslope()
