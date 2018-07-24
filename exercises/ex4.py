def sumN(n):
    total=0
    for i in range (n+1):
        total += i
    print (total)

def sumNCubes(n):
    total=0
    for i in range (n+1):
        total += i*i*i
    print (total)

def main():
    nequal=int(input("Which natural number will be the limit of your set to add up? "))
    sumN(nequal)
    n2equal=int(input("Which natural number will be the limit of your to add up the cubes of? "))
    sumNCubes(n2equal)

    input()
    
main()