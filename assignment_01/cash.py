# This program is meant to determine how much change you will get back using the highest amount first. 
def cashreg(): 
    remainder=eval(input("Please enter the change you owed: "))
    quart=0
    dime=0
    nick=0
    penn=0
    while remainder>=0.25:
        remainder=remainder-0.25
        quart=quart+1
        
    while remainder>=0.10:
        remainder=remainder-0.10 
        dime=dime+1

    while remainder>=0.05:
        remainder=remainder-0.05
        nick=nick+1
        
    while remainder>0.01:
        remainder=remainder-0.01
        penn=penn+1
    
    print ("Your change came out to",penn,"pennies,",nick,"nickels,",dime,"dimes, and",quart,"quarters.")
cashreg()