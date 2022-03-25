# pands-problem-sheet

Number of e’s:

The purpose of the program was to count the number of e’s in the Moby Dick text. It was not specified if I needed to count upper or lower case here so I went on the assumption that it was lower case only as the e in the request was a lower case e.
I used text from https://www.gutenberg.org/files/2701/old/moby10b.txt.
In order to read the text, the program had to take the filename from an argument on the command line. Firstly to do this, I imported the sys module https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python.
I stored the sys.argv[1] as a variable called filename to make it more accessible. This allowed me to run the first argument (which was the moby-dick.txt) https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script#:~:text=argv%5B0%5D%20catches%20the%20directory,have%20a%20example.py%20file.
The code I used for the function was based on the code from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ However, this code did not use the ‘with open’ method, so I had to rewrite some of the code to allow for this.
I defined the function to count the number of lowercase e’s, using the ‘with open ‘command. I opened the file as a read text, as I only wanted to read it. I opened the file as ‘f’ so that from now on the file was named ‘f’. 
After this, I stored what I was looking for in the text, (ie: the number of e’s) as a variable named  ‘numberOfe’s”. Then I wanted the program to return all of the e’s in the text and to do this I used the return command.
All of the code within the defined function was indented.
Finally, I called the whole function to print the number of e’s in the text, ‘f’. I did this by entering .\es.py .\moby-dick.txt in the terminal inside of the PANDS-PROBLEM-SHEET directory. 
The print call was not indented as it was not a section of the defined function.


Plottask.py

The purpose of this program was to plot 3 functions: f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4], on the one set of axes.
Firstly, I imported Numpy and Matplotlib, the modules needed to run this program on Python. These modules are already in Anaconda so I didn’t need to install them. I used Numpy as a faster way of dealing with arrays and the Matplotlib module for plotting the data I was working with.
The xpoints needed to be in a range from 0 to 4 so I used range (0,5) to allow for to be included 4 included when creating my xpoints range.
Next were the y values. As f(x)= x is the same as saying f(x) = y, https:www.youtube.com/watch?v=uWKGVSpWcc8 , I used this basis to create my three values for y. 
•	ypointsA = xpoints, 
•	ypointsB = xpoints2
•	ypointsC = xpoints3

When I had my points generated, I then plotted them. As I was plotting 3 different functions all on the one set of axes, I used the plt.plot function 3 times to plot the three of them. I also researched on how to change the appearance of the plot. I changed the line type https://www.w3schools.com/python/matplotlib_line.asp ,  marker type https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm . I also inputted a grid behind the plots https://www.w3schools.com/python/matplotlib_grid.asp 

I named the x and y axes (x= Range 0-4) and (y = function) and gave the plot a name - Plot of Functions. https://www.w3schools.com/python/matplotlib_labels.asp . I changed the colour of these labels I added a legend to label each of the line plot names and changed the colour of the lines also. 
Finally, to run the program I ran the command plt.show(). This generated visual plot of the three functions I had created. I also saved the plot as a png file using plt.savefig(“Plot Task.png”) so that it could be seen on GitHub when I pushed up the task.





