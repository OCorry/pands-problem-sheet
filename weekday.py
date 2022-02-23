#program to see what day of the week it is 
#Author Orla Corry 
#program last run on Wednesday, 23/02/2022

import datetime #importing datetime funtion to python
x = datetime.datetime.now() #x is equal to the day it is at this moment in time 
today = x.strftime("%A")  #define today as a str (weekday, full version)
#print(today)   #this will print out today's day - if i had put this in inverted commas it would have just printed "today"
                #will tag this out for the purposes of printing a neater final output

if today == "Saturday": #if this statement is false, the elif statement will run 
    print ("It is the weekend, yay!")

elif today == "Sunday": #if this statement is false, the else statement will run 
    print("It is the weekend, yay!")

else:
    print("Yes, unfortunately today is a weekday.") #this is the only option left so if the last 2 statements were both false, this must be true so it must run