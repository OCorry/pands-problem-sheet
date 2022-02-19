#Program to input a string and output every second letter in reverse order
#Author: Orla Corry 

#Using input command to allow me to input the string in the terminal
originalString =input("Please Enter String:")

#Using code [::-2] to print every second string in reverse order
#Reference: https://www.w3schools.com/python/python_howto_reverse_string.asp
newString = originalString [::-2]

print("The New String is :{}" .format(newString))





