# pands-problem-sheet
# Author: Orla Corry 

## ***Introduction*** 

This README.md file gives an description of the seven weekly tasks that I have been working on as part of my Programming and Scripting module. 
It also includes references for all of the sources I have used to help me carry out the seven tasks. 

###### **Week 2: calculate_bmi.py**

The purpose of this program was to calculate BMI. 
Firstly, I used the input() function for the weight and height variables (Sweigart, A. 2015 P.15). This allows the user to input whatever variables they want in the terminal. For the purposes of this task, I was using the variables provided; weight = 65kg and height= 180cm. 
The next step was to research how to calculate the BMI itself. I sourced this from https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g . BMI is (weight in kg) divided by ((height in m)squared). The height value had to be divided by 100 to get height in m as the input value was in cm.
I used the round() function when calculating the BMI, to round the output value to 2 decimal places (Sweigart, A. 2015 P. 338)
Finally, I called the print() function, to complete the program. Using the format() function https://www.w3schools.com/python/ref_string_format.asp , the print() function printed a formatted string “The BMI is (kg/m2) 20.06.”






## **Week 3: secondstring.py**

The purpose of this program was to allow the user to input a sentence and use code to output a second string with every second letter in reverse order. To allow the user to input the sentence (originalSentence) in the terminal, I used the input() function, followed by ‘Please enter a sentence:”.
The next step was to source code to obtain the output requested. To print the secondString in reverse, I got my code from https://www.w3schools.com/python/python_howto_reverse_string.asp. This started at the end of the string and worked backwards. However, as the program also needed to be able to print every second letter in reverse order, so I needed to alter this code. I found code from https://stackoverflow.com/questions/53769570/printing-even-characters-with-strings-in-python to print every second letter. I incorporated the two ideas from the two sources to make [::-2]. Meaning that starting at the very end of the string, the program would output every second letter. If I had used [43::-2], I would have gotten the same output (as there are 43 indexes in the sentence. However, because I was starting from the very end of the sentence in this case, I didn’t need to specify the index number. 
The final step was to call the print() function to print the output of the program in the terminal; .o zletrv pu o wr cu h



## **Week 4: collatz.py**

The purpose of this task was to ask the user to input a positive integer (in this case, using the number 10) and the program was to output values given a set of instructions. At each step, taking the current value and depending on whether it was an odd or even number; either divide the number by 2 or else multiply the number by 3 and add 1, respectively. 
Firstly, I initialised the variable ‘number’ using the input() function so that the user could input the positive integer themselves in the terminal. To ensure that the program recognised that it was an integer I was looking for, I put ‘int’ before the input() function.
I sourced my code for this program from https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e .
I used the ‘if’ and ‘else’ statements for the program. On their own however, they would not generate the output that I was looking for above. The program would have stopped running with an output of 5 as the program would have carried out the ‘if’ statement as the ‘if’ statement was true in this case (Sweigart, A. 2015, P.38). Also, to note here, had the ‘if’ statement been false (ie.: an odd number), the program would have skipped the ‘if’ statement and carried out the else statement instead (Sweigart, A. 2015, P.39).
To overcome the issue above, I used a while loop so that while the value of the number was not equal to 1, the program would continue to run. The code under the while clause will run as long as the condition of the while statement is true (Sweigart, A. 2015, P. 45).
I indented the ‘if’ and ‘else’ statements so that the block of code that I was using ran under the while loop condition I had set.
I also initialised a variable called ‘list’ so that the program would output the list of values from the block of code. I used the append() function so that for each value the program generated, it would be added to the list https://realpython.com/python-append/. I found that in order for initial value (10) to print, I also had to put the append() function before the while loop so that 10, too would be added to the list. 
Finally, I called the function using the print()  function to print the list. The program printed [10, 5, 16, 8, 4, 2, 1]



## **Week 5: weekday.py**

The purpose of this program was to output whether or not the current day was a weekday.  
Firstly, I needed to import the datetime module to python and then, I allocated the variable ‘now’ to the function datetime.datetime.today().weekday(). The today() function was used to establish what day of the week it was currently. The weekday() function was used to get the number of the day of the week. If the number of the day of the week was greater than 5, then it was the weekend, and if it was less than 5, it was a weekday. https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python . Calling this function, returned the day (date and time) as it was on my PC at the moment in time that the program was run (Sweigart, A. 2015 P. 341). 
I used the ‘if’ and ‘else’ statements again for this program. So, as long as the ‘if’ statement was true, then it would run. Otherwise, (had the ‘if’ statement been false) the ‘if’ statement would have been skipped and the ‘else’ statement would run instead (Sweigart, A. 2015 P. 39). 
In order for the program to output a result, under the ‘if’ statement I called print() function to print “Yes, unfortunately today is a weekday.”. Under the ‘else’ statement, I called print() function to print “It is the weekend, yay!” 



## **Week 6: squareroot.py**

The purpose of this program was to get the square root of a floating point number without using any of the built in functions on Python, so instead I used the Newton method to estimate the square root.
Firstly, I initialised the variable ‘n’, (number I was looking for the square root of) as a floating point as the number I was working with for this program is a float, 14.5. I defined n using the input() function so that the user could input the number in the terminal. I defined this inside the function so that it was a local variable rather than a global variable (Sweigart, A. 2015, P. 67). 
Using the code from my source https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx, I went on to calculate the square root of the number. I used the return() function to then exit the function. I also used the round() function here and put the number 1 in the second argument of the function so that the output would round to 1 decimal place (Sweigart, A 2015 P. 338). All this block of code was indented as it is all a sub-part of the defined function.
Finally, I called the print() function to output the result of the defined function. I used the format() function so that the output would be printed as a formatted string https://www.w3schools.com/python/ref_string_format.asp. 
The print() function was not indented as it was not a sub-part of the defined function. The output generated in the terminal was ‘The square root of 14.5 is approx. 3.8.’




## **Week 7: number_of_e’s.py:**

The purpose of the program was to count the number of e’s in the Moby Dick text. It was not specified if I needed to count upper or lower case here so I went on the assumption that it was lower case only as the e in the request was lower case.
I used text from https://www.gutenberg.org/files/2701/old/moby10b.txt.
In order to read the text, the program had to take the filename from an argument on the command line. Firstly to do this, I imported the sys module https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python.
I stored the sys.argv[1] as a variable called filename to make it more accessible. This allowed me to run the first argument (moby-dick.txt) on the command line. If I had for example, changed the number here to [2], it would have given an error as the list index was out of range. This is because there were only index 0 (es.py- ie: the directory where the file is located) and index 1 (moby-dick.txt- ie: the first argument).https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script#:~:text=argv%5B0%5D%20catches%20the%20directory,have%20a%20example.py%20file.
The code I used for the function was based on the code from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ However, this code did not use the ‘with open’ method, so I had to rewrite some of the code to allow for this. Using the ‘with open’ statement means that the file will automatically close again https://www.pythonforbeginners.com/files/with-statement-in-python. 
I defined the function and using the ‘with open ‘command. I opened the file as ‘rt’ (read text), as I only wanted to read it. I opened the file as ‘f’ so that from now on the file was named ‘f’. 
I then stored f.read() as a variable called data. I left the brackets after f.read() blank here as I wanted the program to read the whole text https://www.w3schools.com/python/ref_file_read.asp.  
Next, I used the return keyword to exit the function and to return a value from the function https://www.w3schools.com/python/ref_keyword_return.asp.  Following the return keyword, I used data.count(letter) as I wanted the program to return a count of the letters in the text https://www.w3schools.com/python/ref_list_count.asp. 
All of the code within the defined function was indented as it was all a sub-part of the function.
Finally, I called the whole function by using print() and requested that the number of ‘e’s in the text, ‘f’. be printed. I did this by entering .\es.py .\moby-dick.txt in the terminal. 
The print call was not indented as it was not a section of the defined function. The print() call printed an output of 116960 lower case e’s.



## **Week 8: plottask.py**

The purpose of this program was to plot 3 functions: f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4], on the one set of axes.
Firstly, I imported Numpy and Matplotlib, the modules needed to run this program on Python. These modules are already in Anaconda so I didn’t need to install them. I used Numpy as a faster way of dealing with arrays and the Matplotlib module for plotting the data I was working with.
The xpoints needed to be in a range from 0 to 4 so I used range (0,5) to allow for 4 to be included when creating my xpoints range.
Next were the y values. As f(x)= x is the same as saying f(x) = y, https:www.youtube.com/watch?v=uWKGVSpWcc8 , I used this basis to create my three values for y.

•	ypointsA = xpoints, 

•	ypointsB = xpoints(squared),

•	ypointsC = xpoints(cubed)

When I had my points generated, I then plotted them. As I was plotting 3 different functions all on the one set of axes, I used the plt.plot function 3 times to plot the three of them. I also researched on how to change the appearance of the plot. I changed the line type https://www.w3schools.com/python/matplotlib_line.asp,  marker type https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm on the plots. I also inputted a grid behind the plots https://www.w3schools.com/python/matplotlib_grid.asp.

I named the x and y axes (x= Range 0-4) and (y = function) and gave the plot a name - Plot of Functions https://www.w3schools.com/python/matplotlib_labels.asp. I changed the colour of these labels and I added a legend to label each of the line plot names and changed the colour of the lines also. 
Finally, to run the program I ran the command plt.show(). This generated visual plot of the three functions I had created. I also saved the plot as a png file using plt.savefig(“Plot Task.png”) so that it could be seen on GitHub when I pushed up the task.




# ***List of references accessed:***


## **Week 2: calculate_bmi.py**

https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g

https://www.w3schools.com/python/ref_string_format.asp

Sweigart, A. (2015) “Automate The Boring Stuff With Python”

## **Week 3: secondstring.py**

https://www.w3schools.com/python/python_howto_reverse_string.asp

https://stackoverflow.com/questions/53769570/printing-even-characters-with-strings-in-python


## **Week 4: collatz.py**

https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e

https://realpython.com/python-append/

Sweigart, A. (2015) “Automate The Boring Stuff With Python”


## **Week 5: Weekday.py**

https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python

Sweigart, A. (2015) “Automate The Boring Stuff With Python”


## **Week 6: squareroot.py**

https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx

https://www.w3schools.com/python/ref_string_format.asp

Sweigart, A. (2015) “Automate The Boring Stuff With Python”


## **Week 7: number_of_e’s.py:**

https://www.gutenberg.org/files/2701/old/moby10b.txt

https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python

https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script#:~:text=argv%5B0%5D%20catches%20the%20directory,have%20a%20example.py%20file

https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

https://www.pythonforbeginners.com/files/with-statement-in-python

https://www.w3schools.com/python/ref_file_read.asp

https://www.w3schools.com/python/ref_keyword_return.asp

https://www.w3schools.com/python/ref_list_count.asp


## **Week 8: plottask.py**

http://www.youtube.com/watch?v=uWKGVSpWcc8

https://www.w3schools.com/python/matplotlib_line.asp

https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

https://www.w3schools.com/python/matplotlib_grid.asp

https://www.w3schools.com/python/matplotlib_labels.asp

Sweigart, A. (2015) “Automate The Boring Stuff With Python"

## **README.md file**
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax




