#Program to input a string and output every second letter in reverse order
#Author: Orla Corry 

#Using input command to allow me to input the string in the terminal
originalString =input("Please Enter String:")

#Using code [0::2] to output every second letter from the string, beginning with the fist even character
#If I were to use code [1::2] here instead, every second letter from the string, staring with the first odd characer would be printed
#Refernce: https://stackoverflow.com/questions/53769570/printing-even-characters-with-strings-in-python

#Using code [::-1] to print the string in reverse order
#Reference: https://www.w3schools.com/python/python_howto_reverse_string.asp
newString = originalString [0::2] [::-1]

print("The New String is :{}" .format(newString))





