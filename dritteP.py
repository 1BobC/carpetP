#This file will be re-used for python programs from Code-camp Python for Everybody
#3:20:00 ish Ch 7 Reading files, opening files, fhandle, newline character, File processing
#fhandle as a sequence using a for loop to iterate through the sequence (NB a sequence is an oredered set)
#eg (elegance!) xfile = open('mbox.text')
#               for cheese in xfile :
#                   print(cheese)

# fhand = open('mbox.txt')
# count = 0
# for line in fhand :
#     count = count + 1
#     print("Line count: ", count)

#ok, runs if I cd to carpetP in python3 terminal
#How do I get Run in file terminal to work? EG:

# fhand = open('mbox-short.txt')
# for line in fhand :
#     if line.startswith('From:') :
#         print(line)

#File --> Preferences --> Settings --> (User)Extensions --> Python -->Terminal: Execute In File Dir --> Check It

#Reading the *whole* file 3:38:42
# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print("file length: ", len(inp), "lines")

# print("Input at line 20 is:", inp[:20])

#Searching through a file with if in the for loop
# fhand = open('mbox-short.txt')
# for line in fhand :
#     line = line.rstrip()   #the print statement adds a \n, hence the blank lines between Froms, fix this (no blank lines)
#     if line.startswith("From") :
#         print(line)

#Skipping lines with continue 3:43:23





