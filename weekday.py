#Write a program that outputs whether or not today is a weekday
#Author: Orla Corry 

import datetime #importing datetime funtion to python
now = datetime.datetime.today().weekday() #now is equal to the day and time it is at this moment in time 

if now < 5: #if the number of the day of the week is less than 5 it is a weekday 
    print("Yes, unfortunately today is a weekday.")

else: #if the number of the day of the week is greater than five (Saturday or Sunday, it is the weekend)
    print("It is the weekend, yay!")
