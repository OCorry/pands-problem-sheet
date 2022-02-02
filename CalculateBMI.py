# Program to calculate BMI
# Read in variables using Input 
# Orla Corry 
weight = int(input("Enter Your weight:"))
height = int(input("Enter Your height:"))
# Dividing height by 100 and then calculating this answer to the power of 2 to get meters squared 
BMI = weight / (height/100)**2
# Each {} represents the two inputs (weight and height) and the Output, (BMI)
print ('{} equal {} divided by {} '.format(BMI, weight, (height/100)**2))