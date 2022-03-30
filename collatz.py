#program that asks user to input a positive integer 
#and outputs the successive values of the following calculation:
#at each step, calculate the next value by taking the current value and, if its even, multiply by 2
#but if its odd, multiply it by 3 and add 1

#Author: Orla Corry

            
number = int(input("Please enter a positive integer:"))

list = [] #the program needs to output a list of the numbers that the block of code creates
list.append(int(number)) #adding a number to the list each time a number genterated
                            #Using int() so output will be as an integer

while number != 1: #while the number is not equal to 1
    if number % 2 == 0: #if the number divides by two with no remainder (ie: an even number)
        number = number / 2
        list.append(int(number)) #to add the number to the list 
    else: #if number is an odd number 
        number = (3 * number) + 1
        list.append(int(number)) #to add the number to the list 

#calling the function using print() command 
print(list)




        



    


    