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

#Searching through a file with if in the for loop 1st way
# fhand = open('mbox-short.txt')
# for line in fhand :
#     line = line.rstrip()   #the print statement adds a \n, hence the blank lines between Froms, fix this (no blank lines)
#     if line.startswith("From") :
#         print(line)

#Skipping lines with continue 3:43:23 Nice reverse two step. Read carefully! 2nd way
# fhand = open('mbox-short.txt')
# for line in fhand :
#     line = line.rstrip()        #so far the same as above
#     if not line.startswith('From:') :
#         continue
#     print(line)
    
#and another using in to select lines   3rd way
# fhand = open('mbox-short.txt')
# for line in fhand :
#     line = line.rstrip()
#     if not '@uct.ac.za' in line :   #see the difference?
#         continue
#     print(line)
        
#prompt file name as input
# fname = input("Enter the filename:   ")
# fhand = open(fname)
# count = 0
# for line in fhand :
#     if line.startswith('From: ') :
#         count = count + 1
# print("There are", count, "'From:' lines in", fname)    

#Bad file names start 3:46:19
# fname = input("Enter the file name: ")
# try :
#     fhand = open(fname)
# except :
#     print("File name", fname, "cannot be opened! Best to check the file name.")
#     quit()
    
# count = 0
# for line in fhand :
#     if line.startswith("Subject:") :
#         count = count + 1
# print("There are", count, "'Subject:' lines in", fname)

#Files Summary - Secondary storage, Searching for files, Opening files fhand, Reading file names, File structure \n, Dealing with BAD FILES, Reading files line by line with a loop.

#3:49:00  Ch8  Lists (Data) - Programming Algorithms V Data Structures         
#Variables hold one value which may be changed, a Collection / List variable holds many values usually in square brackets.
#a collection / list may contain any python object or be empty!
#Remember:
# for i in [5, 4, 3, 2, 1] :
#     print(i)
# print("Blast off!")

#Also be aware of the names of the variables, not necessarily descriptive - see below:
#Lists and definite loops 3:53:00
# friends = ['Ben', 'Shona', 'Freya']
# for friend in friends :
#     print("Happy New Year:", friend)
# print("Done!")

# z = ['June', 'Bob', 'Abraham']
# for x in z :
#     print("Happy Christmas:", x)
# print('Finished!')

#Looking inside lists 3:54:11
# friends = ['Harry', 'Megan', 'Charles']

#Lists are mutable, strings are not - watch out!
# fruit = 'BANANA'
# #fruit[0] = 'b'
# x = fruit.lower()
# print(x)

# lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lotto)
# lotto[2] = 31
# print(lotto)
# lotto[5] = 61
# print(lotto)
# #we used the index operator eg lotto[2] = 31

# #How long is a list? how many elements? - String list or object list
# greet = "Hello, Bob, June, Kelly, ShonaR, ShonaC"
# print(len(greet))

# nums = [21, 23, 34, 45, 'Fred', 56, 67, 'Jim', 78, 89]
# print(len(nums))

#3:56:56 Using the range function
# print(range(4))
# for i in range(4) :
#     print(i)
    
#friends = ['Harry', 'Sally', 'Harry']
# print(len(friends))
# print(range(len(friends)))

# for i in range(len(friends)) :
#     print(i)

#Two loops using range
# friends = ['Harry', 'Sally', 'Harry']

# for friend in friends :
#     print("Happy New  Year", friend)
    
# for i in range(len(friends)) :
#     friend = friends[i]
#     print("Happy This Year", friend)
    
#3:59:46 Loop operations
#Concatanating lists using +
# a = [10, 20, 'drink', 40, 50]
# b = ['gargle', 70, 80, 90]
# c = a + b
# print(c)
# print(a)

#List Slicing with :
# t = [23, 'handy', 45, 'werde', 98, 12, 'Handel']
# print(t[1:4])
# print(t[:2])
# print(t[:])

#List methods
# x = list()
# print(type(x))
# print(dir(x))

#4:02:37 Building a list from scratch
# stuff = list()
# stuff.append('Granta146')
# stuff.append(146)
# print(stuff)
# stuff.append("Fruit Cake")
# print(stuff)
 
#Two logical operators (True / False) to check what is in a list
# some = [11, 22, 33, 44, 55, 66, 77]
# print(9 in some)
# print(33 in some)friends = ['Garth', 'Vader', 'Scotty']
# print(8 not in some)

#Lists are in order - here's some list play - sort, append, insert!
# friends = ['Garth', 'Vader', 'Scotty']
# print(friends)
# friends.sort()      #changes the list order 
# print(friends)[
# print(friends[2])
# friends.insert(1, 'Harry')      #OK google search needed!!
# print(friends)
# friends.append('Jacob')
# print(friends)
# print('Jeremy' not in friends)

#4:05:07 Built in  list functions:
#print(dir(friends))
# print(friends[1])
# friends.sort()
# print(friends[2])
# print(friends)

#4:06:07 more built in function to find average of inputs
#Average 1:
# total = 0
# count = 0
# while True :
#     inp = input("Enter a number: ")
    
    
#     if inp == "done" :  #note - inp not input!
#         break 
#     value  = float(inp)
#     total = total + value
#     count = count + 1
    
# average = total / count
# print("Average is: ", average)

#Average 2:
# numlist = list()
# while True :
#     inp = input("Enter a number:  ")
#     if inp == "done" : break
#     value = float(inp)
#     numlist.append(value)
    
# average = sum(numlist) / len(numlist)
# print("Average is: ", average)

#4:09:07 Summary - how strings and lists are related (!)
#The Split function - Strings and Lists yeah!
#See also find and slice - mmmm...
# abc = "With three words"
# stuff = abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[1])

# #and more from split on...
# print(stuff)
# for w in stuff :
#     print(w)

#Looking closer at spaces and other places to split
# line = "A lot         of       spaces"  #split equalises the spaces...
# etc = line.split(' ')       #also try with no delimiter specified
# print(etc)
# print(len(etc))
# #now with semicolons
# line = "semicolons;instead;of;spaces"
# thing = line.split()
# print(thing)
# print(len(thing))
# thing = line.split(';')
# print(thing)
# print(len(thing))

#04:13:55 digging deeper eg...
#eg. fom mbox-short.txt From stephen.mquard@uct.ac.za Sat Jan 5 09:14:16 2008 
# fhand = open('mbox-short.txt')
# for line in fhand :
#     line = line.rstrip()
#     if not line.startswith('From ') : continue
#     words = line.split()
#     print(words[2])
    
#split by spaces is:
# line = 'From stephen.mquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words = line.split()
# print(words)

#Ok now for the Double Split ie split once then split a bit of the split!!
line = 'From stephen.mquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]    
print(email)        #stephen.mquard@uct.ac.za 
pieces = email.split('@')
print(pieces)
print(pieces[0])
print(pieces[1])
#List Summary and move on to data structures
#4:17:56 The Guardian Pattern - when I find the exercise files! See file dow.py 

#4:29:01 Back to dritte.py for Ch 8 Dictionaries
