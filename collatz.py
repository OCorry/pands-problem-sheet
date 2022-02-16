#program that asks user to input a positive integer 
#and outputs the successive values of the following calculation

#at each step calcultae the next value by taking the current value and, if its even, multiply by 2
#but if its odd, multiply it by 3 and add 1

#Author: Orla Corry
number =int(input("enter a number:"))

while number!=1: 
    if(number % 2) == 0:
        number = number/2
        print (number)
     
    else:
        number = ((number*3)+1)
        print(number)

        



    


    