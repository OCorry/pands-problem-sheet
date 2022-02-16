#program that asks user to input a positive integer 
#and outputs the successive values of the following calculation

#at each step calcultae the next value by taking the current value and, if its even, multiply by 2
#but if its odd, multiply it by 3 and add 1

#Author: Orla Corry
number =int(input("enter a number:")) #initialising variable and using input statement so i can input in terminal

while number!=1: #while loop will continue running as long as the value doesnt equal to 1
    if(number % 2) == 0: #if value is an even number
        number = number/2 #then divide the number by 2
        print (number)
     
    else: #or else, if the value is an odd number 
        number = ((number*3)+1) #muliply the value by 3 and then add 1
        print(number)

        



    


    