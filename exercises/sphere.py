import math 
def sphereArea(radius):
    A=4*math.pi*radius**2 
    print (A, "units")
    
def sphereVolume(radius):
    V=(4.0/3.0)*math.pi*radius**3 
    print (V,"units")
    
def solve():
    ainput= eval(input("What is the radius of the sphere you would like to find the surface area of? "))
    sphereArea(ainput)
    vinput= eval(input("What is the radius of the sphere you would like to find the volume of? "))
    sphereVolume(vinput)
solve()