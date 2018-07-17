#Computes the nth Fibonacci number of the sequence.
def fibby():
    p = eval(input("What term of the Fibonacci Sequence do you desire? "))
    k=[0,1]
    for i in range(2,p):
             k.append(k[i-2]+k[i-1])
    print ("The",p,"term of the sequence is",(k[p-1]),".")

         
fibby()