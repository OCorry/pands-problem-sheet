#Write a program that reads in a text file from the command line and outputs the number of e's it contains
#I am assuming that the user is looking for the number of lower case e's as it is lowecase in the request and they dont specify
#Author: Orla Corry 

'''
#I did this first simply to make sure the file would read before moving on to researching the letter counting part of the task
import sys 
with open(sys.argv[1], 'rt') as f:
    #data = f.read()  #storing f.read() in a variable called data so it is more accessable
print (data)
https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python
'''

import sys #need to import sys module to be able to read in a file from the command line

filename = sys.argv[1]  #using variable filename so it is more accessable
                        #inputting [1] so that the first argument is taken on the command line 

def letterFrequency(f, letter): #defining the function
    
    with open(filename, 'rt') as f: #open the file in read text mode as 'f'
 
         data = f.read() #using text as variable for the file 'f' leaving the read() blank so the whole text is read
 
         return data.count(letter) #using count() function to count number of letters 
         
        
print(letterFrequency('f', 'e')) #Calling the function to print out the number of lower case e's in the .txt file
                                #Dont need to specifically define that it's lower case here as Python is case sensitive anyway 
                                
                                


