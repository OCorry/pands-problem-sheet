#Program to input a sentence (str) and output every second letter in reverse order
#Sentence: The quick brown fox jumps over the lazy dog.
#Author: Orla Corry 

#Read in the variable using input() function so that user can input string in the terminal
originalSentence =input("Please enter a sentence:")

#Using code [::-2] to print every second letter in reverse order
secondString = originalSentence [::-2]

#(secondString = originalSentence [8::-2] # I only did this to check my understanding of the code was correct, 
#and that the output would start with 8th index, k )

#calling the print() function to output the program 
print (secondString)





