#Thierno Aziz Diallo
#Week 7 task.
"""
Write a program that reads in a text file and outputs the number of e's it contains.
The program should take the filename from an argument on the command line
"""
#Define Functions
def look_for_file(fileName):

    with open(fileName, 'r') as f: #read file 
        count = 0 #counting how many characters 'E' will appear starting by ZERO
        
        for line in f: # Getting a line line one by one
            for character in list(line): #Creating a list with the lines and sweep it
                if (character == 'e'): # this compares each characters from the list with 'e'
                    count = count + 1 #found and summarize the counting 
                    

        return count #Returning functions

#Main Problem
fileName = str(input("Type the file Name:")) #calling my file ()

print('Found', look_for_file(fileName)) #prints the number of e from the whole text.
