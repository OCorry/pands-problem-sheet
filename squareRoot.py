#Program to find the square root of a positive floating point number 
#Inputting the positive floating point number and outputting approximation of its sqr root
#Not using the built in square root function
#Using Newton's formula
#Author: Orla Corry 
n = float(input("Enter a number:")) #allows user to input a floating point number

def newtonSqrt(n, base): #defining the Newton function 
    approx_root = 0.5 * n
    for i in range(base):
        betterapprox = 0.5 * (approx_root + n/approx_root)
        approx_root = betterapprox
    
    return round(betterapprox, 1) #exiting the function to allow python to run the rest of the program
                                #(ie to call the function)  
                                # Using round here to round the decimal place to one           

print("the square root of 14.5 is approximately:",newtonSqrt(14.5,10)) #calling the function so that it will run 