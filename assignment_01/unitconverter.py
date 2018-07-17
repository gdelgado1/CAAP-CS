def unitconverter(): 
    #This is converter for miles to inches. 
    Miles= eval(input("Enter the number of miles: "))
    Inches= Miles * (63360)
    Inches= round(Inches,10)
    print ("There are",Inches,"Inches in",Miles,"miles.")
unitconverter()