#Write a program that reads in a text file and outputs the number of e's it contains
#I am assuming that the client is looking for the number of lower case e's as it is lowecase in the request and they dont specify
#Author: Orla Corry 

#I did this first simply to make sure the file would read before moving on to researching the letter counting part of the task
#import sys 
#with open(sys.argv[1], 'rt') as f:
#data = f.read()  #using f.read() as a variable  data so it is more accessable
#print (data)
#https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python


import sys #need to import sys to be able to read a file from command line
#https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
filename = sys.argv[1]  #storing this in a variable called filename so it is more accessable

def letterFrequency(f, letter): #defining the function
    
    with open(filename, 'rt') as f: #open the file in read text mode 
 
    # store content of the file in a variable
         numberOfEs = f.read() #storing what we are looking for in the file as a variable 
 
         return numberOfEs.count(letter) 
        #Calling the function to print out the number of lower case e's in the txt file
 
print(letterFrequency('f', 'e')) #dont need to specifically define that it's lower case here as Python is case sensitive anyway 

#https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/