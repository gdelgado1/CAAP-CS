# Gustavo Delgado
# Assignemnt X
# Due August 5th 

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")

# setting out box sizes to the n sq pixels per box
boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle.
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This should change according to the image size you want to make and the size of your boxes ("pixels")
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
myPen.penup()
myPen.forward(-200)
myPen.setheading(90)
myPen.forward(200)
myPen.setheading(0) 

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
	myPen.begin_fill()
	# 0 deg.
	myPen.forward(intDim)
	myPen.left(90)
	# 90 deg.
	myPen.forward(intDim)
	myPen.left(90)
	# 180 deg.
	myPen.forward(intDim)
	myPen.left(90)
	# 270 deg.
	myPen.forward(intDim)
	myPen.end_fill()
	myPen.setheading(0)       

# Here is an example of how to draw a box using the box function      
# Comment this out when you draw your own images
box(boxSize)
 

# Challenge functions (2 bonus pts each) 
# You need to make shapes with each
#def circle(intRadius):
#def triangle(intLength): #This can be an equilateral triangle
#def save_image(): # saves the screen to an image/vector file

# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings as lists.
# This first list stores the color values

# Your drawings are stored using a "list of lists" where each value within every list
# element is the index of the color in the pallet list

# Banana
pallet_1 = ["#FFFFFF" , "#FFFF00" , "#000000" , "#61380B" , "#F4FA58"]
pixels_1 =     [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_1.append([0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,2,2,3,3,2,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,4,1,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,4,1,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,1,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,1,1,2,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,1,3,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# Mario
pallet_2 = ["#4B610B" , "#FAFAFA" , "#DF0101" , "#FE9A2E"]
pixels_2 =     [[1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1]]
pixels_2.append([1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_2.append([1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1])
pixels_2.append([1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1])
pixels_2.append([1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3])
pixels_2.append([1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1])
pixels_2.append([1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1])
pixels_2.append([1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1])
pixels_2.append([1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1])
pixels_2.append([0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0])
pixels_2.append([3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3])
pixels_2.append([3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3])
pixels_2.append([3,3,3,2,2,2,2,1,1,2,2,2,2,3,3,3])
pixels_2.append([1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1])
pixels_2.append([1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1])
pixels_2.append([0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0])

#Ghost
pallet_3 = ["#FFFFFF","#2461D5","#D5B824","#000000"] 
pixels_3 =     [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_3.append([0,0,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0])
pixels_3.append([0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0])
pixels_3.append([0,0,2,2,2,0,0,2,2,2,2,2,0,0,2,2,0,0])
pixels_3.append([0,2,2,2,0,0,0,0,2,2,2,0,0,0,0,2,2,0])
pixels_3.append([2,2,2,2,0,0,0,0,2,2,2,0,0,0,0,2,2,2])
pixels_3.append([2,2,2,2,0,0,0,0,2,2,2,0,0,0,0,2,2,2])
pixels_3.append([2,2,2,2,0,1,1,1,2,2,2,0,1,1,1,2,2,2])
pixels_3.append([2,2,2,2,0,1,1,1,2,2,2,0,1,1,1,2,2,2])
pixels_3.append([2,2,2,2,0,1,1,1,2,2,2,0,1,1,1,2,2,2])
pixels_3.append([2,2,2,2,0,1,1,1,2,2,2,0,1,1,1,2,2,2])
pixels_3.append([2,2,2,2,2,0,0,2,2,2,2,2,0,0,2,2,2,2])
pixels_3.append([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
pixels_3.append([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
pixels_3.append([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
pixels_3.append([2,2,2,0,2,2,2,2,0,0,2,2,2,2,0,2,2,2])
pixels_3.append([2,2,2,0,2,2,2,2,0,0,2,2,2,2,0,2,2,2])
pixels_3.append([2,2,0,0,0,2,2,0,0,0,0,2,2,0,0,0,2,2])

#Virus 
pallet_4 = ["#FFFFFF", "#F3E5F8","#716575"]
pixels_4 =     [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_4.append([0,0,2,1,1,0,0,0,0,0,0,0,2,2,2,2,2,1,1,0,0])
pixels_4.append([0,0,2,1,1,1,1,1,0,0,0,0,2,2,1,1,1,1,1,0,0])
pixels_4.append([0,0,2,2,2,1,1,1,0,0,0,0,2,2,1,1,1,0,0,0,0])
pixels_4.append([0,0,0,2,2,1,1,1,2,2,2,2,2,2,1,1,1,0,0,0,0])
pixels_4.append([0,0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0])
pixels_4.append([0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
pixels_4.append([2,2,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1])
pixels_4.append([2,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1])
pixels_4.append([2,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1])
pixels_4.append([2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_4.append([2,1,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1])
pixels_4.append([2,1,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1])
pixels_4.append([2,1,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,0,2,1,1])
pixels_4.append([2,1,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1])
pixels_4.append([2,1,1,0,2,1,1,0,0,0,0,0,0,0,2,1,1,0,0,1,1])
pixels_4.append([0,0,0,0,2,1,1,0,0,0,0,0,0,0,2,1,1,0,0,1,1])
pixels_4.append([0,0,0,0,0,0,2,1,1,1,0,0,1,1,1,0,0,0,0,0,0])
pixels_4.append([0,0,0,0,0,0,2,1,1,1,0,0,1,1,1,0,0,0,0,0,0])
pixels_4.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_4.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
#Mushroom 
pallet_5 = ["#FFFFFF","#DA2F03","#000000"]
pixels_5 =     [[0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0]]
pixels_5.append([0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0])
pixels_5.append([0,0,0,2,2,2,2,2,1,1,1,1,1,1,0,0,0,2,2,2,2,2,0,0,0,0])
pixels_5.append([0,0,0,2,2,2,2,2,1,1,1,1,1,1,0,0,0,2,2,2,2,2,0,0,0,0])
pixels_5.append([0,0,2,2,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,2,2,0,0])
pixels_5.append([0,0,2,2,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,2,2,0,0])
pixels_5.append([0,2,2,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,2,2,0])
pixels_5.append([0,2,2,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,2,2,0])
pixels_5.append([2,2,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,2,2])
pixels_5.append([2,2,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,2,2])
pixels_5.append([2,2,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,2,2])
pixels_5.append([2,2,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,2,2])
pixels_5.append([2,2,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2])
pixels_5.append([2,2,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2])
pixels_5.append([2,2,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2])
pixels_5.append([2,2,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,2,2])
pixels_5.append([2,2,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,2,2])
pixels_5.append([2,2,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,2,2])
pixels_5.append([2,2,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,1,1,2,2])
pixels_5.append([0,0,2,2,2,2,0,0,0,2,2,0,0,0,0,2,2,0,0,2,2,2,2,2,0,0])
pixels_5.append([0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0])
pixels_5.append([0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0])
pixels_5.append([0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0])
pixels_5.append([0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0])
pixels_5.append([0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0])
pixels_5.append([0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0])

#Smiley 
pallet_6 = ["#FFFFFF","#000000","#F9EA1B","#8B5B15","#E991C0"]
pixels_6 =     [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_6.append([0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0])
pixels_6.append([0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0])
pixels_6.append([0,0,0,1,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,1,1,0,0,0])
pixels_6.append([0,0,0,1,2,1,1,1,1,1,0,1,2,2,2,2,2,2,1,1,1,1,0,0,1,2,2,1,0,0,0])
pixels_6.append([0,0,1,1,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_6.append([0,0,1,2,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_6.append([0,1,2,2,2,1,1,1,1,0,0,0,1,2,2,2,2,1,1,1,1,0,0,0,0,1,2,2,2,1,0])
pixels_6.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,0])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([0,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_6.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0,0])
pixels_6.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,3,3,3,3,1,2,2,1,0,0])
pixels_6.append([0,0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,3,3,1,2,2,1,0,0,0])
pixels_6.append([0,0,0,1,2,2,2,1,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,1,2,2,2,1,0,0,0])
pixels_6.append([0,0,0,0,1,2,2,2,1,1,3,3,3,3,4,4,4,4,4,4,4,1,1,2,2,2,1,0,0,0,0])
pixels_6.append([0,0,0,0,0,1,2,2,2,2,1,1,1,3,4,4,4,4,1,1,1,2,2,2,2,1,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,1,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
#Flower
             #WHITE   #D-ORANGE  #GREEN   #D-GREEN  #L-GREEN   #YELLOW    #RED
pallet_7 = ["#FFFFFF","#EA6C20","#178C1E","#0F6814","#72E978","#DCDC37","#EC4A06"]
pixels_7 =     [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,4,4,0,0,1,1,1,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,4,4,0,1,1,5,5,1,1,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,1,1,1,4,4,1,5,5,5,5,5,1,0,0,0,0])
pixels_7.append([0,0,0,0,1,5,5,1,1,4,4,5,5,5,5,5,1,0,0,0,0])
pixels_7.append([0,0,0,0,1,5,5,5,1,4,4,1,5,5,5,1,1,0,0,0,0])
pixels_7.append([0,0,3,3,1,5,5,1,1,2,4,1,1,5,1,1,0,0,0,0,0])
pixels_7.append([0,2,2,2,3,1,5,5,1,2,2,6,1,1,1,1,1,1,0,0,0])
pixels_7.append([3,2,3,3,3,1,1,1,6,6,2,6,1,5,5,5,5,5,1,0,0])
pixels_7.append([3,2,3,1,5,5,1,1,1,6,6,1,1,1,1,5,5,5,1,0,0])
pixels_7.append([0,0,3,1,5,5,5,5,1,5,1,5,1,5,5,5,5,5,1,0,0])
pixels_7.append([0,0,0,1,5,5,5,1,1,5,1,5,5,1,1,5,5,5,1,0,0])
pixels_7.append([0,0,0,0,1,1,1,1,1,5,5,5,5,1,1,1,5,5,1,0,0])
pixels_7.append([0,0,0,0,3,3,3,1,5,5,5,5,5,1,0,1,1,1,0,0,0])
pixels_7.append([0,0,0,3,2,3,3,1,1,5,5,5,5,1,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,2,3,2,3,3,1,1,1,1,1,0,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_7.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#HummingBird 
			#WHITE    #RED      #BLACK    #D-GREEN  #L-GREEN
pallet_8 = ["#FFFFFF","#B6231A","#000000","#2F8025","#89C782"]
pixels_8 =     [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_8.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3])
pixels_8.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,0])
pixels_8.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0])
pixels_8.append([0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,4,3,3,0,0])
pixels_8.append([0,0,0,0,0,0,4,4,4,0,0,0,0,0,4,3,3,3,0,0])
pixels_8.append([0,2,2,2,2,4,4,2,4,4,0,0,0,4,4,3,3,0,0,0])
pixels_8.append([0,0,0,0,0,1,1,1,1,4,4,0,4,4,3,3,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,1,1,1,1,1,4,4,3,3,3,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,1,0,0,4,4,4,3,3,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,3,3,0,0])
pixels_8.append([0,0,0,0,0,0,4,4,4,4,4,4,4,0,0,4,3,0,0,0])
pixels_8.append([0,0,0,0,0,4,4,4,3,3,0,4,0,0,4,4,3,3,3,0])
pixels_8.append([0,0,0,0,3,3,3,3,3,0,0,0,3,4,4,4,4,3,0,0])
pixels_8.append([0,0,0,3,3,3,3,0,0,0,0,3,3,3,3,4,4,3,3,0])
pixels_8.append([0,0,3,3,0,0,0,0,0,0,0,0,3,0,3,3,3,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_8.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

def draw(pallet, pixels):
	myPen.setheading(0)
	for row in pixels: 
		for color in row:
			myPen.color(pallet[color])
			box(boxSize)
			myPen.forward(boxSize)
		myPen.penup()
		myPen.forward(-1 * len(pixels) * boxSize)
		myPen.setheading(270)
		myPen.forward(boxSize)
		myPen.setheading(0)
	

# Should give the user a list of the possible drawing pieces you have and ask which one to draw
def main():
	pic = int(input("What image would you like to see? Type one of the following assigned digits: \n 1 - Banana \n 2 - Mario \n 3 - Ghost \n 4 - Virus \n 5 - Mushroom \n 6 - Smiley \n 7 - Flower \n 8 - HummingBird"))
	if pic == 1: 
		draw(pallet_1, pixels_1)
	elif pic == 2: 
		draw(pallet_2, pixels_2)
	elif pic == 3: 
		draw(pallet_3, pixels_3)
	elif pic == 4: 
		draw(pallet_4, pixels_4)
	elif pic == 5: 
		draw(pallet_5, pixels_5)
	elif pic == 6:
		draw(pallet_6, pixels_6)
	elif pic == 7:
		draw(pallet_7, pixels_7)
	elif pic == 8: 
		draw(pallet_8, pixels_8)
	else: 
		print ("This is not an accepted value. The program will now end.")
	# You need this to prevent the window from closing after drawing
	turtle.done()

main()