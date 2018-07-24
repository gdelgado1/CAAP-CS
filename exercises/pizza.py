import math
def pizzaca(radius,cost):
    A=math.pi*(radius)**2
    print (A,"sq in.")
    C=A*cost
    print ("")
    print ("$",round (C, 2), "per sq. in.")
    
def main():
    rad=eval(input("What is the radius of the pizza you are consuming? "))
    co=eval(input("What is the cost per square inch of the pizza? "))
    print ("")
    pizzaca(radius=rad,cost=co)
    input()

main()
