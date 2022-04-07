#Write a program to find the square root of a positive floating point number 
#Inputting the positive floating point number and outputting approximation of its sqr root
#Not using the built in square root function
#Using Newton's formula
#squareRoot = 0.5 * (Q + (N / Q))
#Author: Orla Corry 

def newtonSqrt(n, base): #defining the Newton function
    n = float(input("Please enter a positive number:")) #allows user to input a floating point number
                                                       #defining n inside the function so that it is not a global variable
    
    approx_root = 0.5 * n
    for i in range(base):
        betterapprox = 0.5 * (approx_root + n/approx_root)
        approx_root = betterapprox
        
    return round(betterapprox, 1) #exiting the function to allow python to run the rest of the program
                                 # Using round() function here to round the output to 1 decimal place
                                   

print("The square root of 14.5 is approx. {}." .format (newtonSqrt(14.5,10))) #calling the function so that it will run in the terminal  
