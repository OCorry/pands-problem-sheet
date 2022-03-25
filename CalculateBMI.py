# Program to calculate BMI
# Read in the weight and height variables using the input() fumction  
# Author: Orla Corry 

weight = int(input("Enter weight (kg):"))  
height = int(input("Enter height (cm):"))  

#Calculate BMI: weight (kg)/{height (m)}^2
#Dividing height by 100 to convert to meters
BMI = round(weight / (height/100)**2 ,2) #Using the round function to round the output to 2 decimal places

#calling the print() function and using format() function to format the output string 
print ('The BMI is (kg/m2) {}.' .format(BMI)) 
