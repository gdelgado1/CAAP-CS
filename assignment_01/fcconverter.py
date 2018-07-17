def fcconverter(): 
    #This is a converter for Fahrenheit to Celsius temperatures. 
    #Hope you enjoy! 
    Fahrenheit= int(input("Enter a temperature in Farenheit: "))
    Celcius= (Fahrenheit-32)*(5.0/9.0)
    Celcius= round(Celcius,4)
    for i in range(5):
        print ("Temperature:",Fahrenheit,"Fahrenheit =",Celcius,"C.")
fcconverter()