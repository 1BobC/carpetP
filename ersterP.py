#This file will be re-used for python programs from Code-camp Python for Everybody 
#1:20:51 - US elevator floor app - first 'meaningful' program!
# inp = input("Europe floor?")
# usf = int(inp) + 1
# print("US floor", usf)

#Practise blocks and indentation
# x = 5
# if x > 2:
#     print("Bigger than 2")
#     print("Still bigger")
# print("Done with 2")

# for i in range(5) :
#     print(i)
#     if i > 2 :
#         print("Bigger than 2")
#     print("Done with i", i)
# print("All done!")

# #and another...
# x = 42
# if x > 1 :
#     print("Greater than 1")
#     if x < 100 :
#         print("Less than 100")
# print("All done!")

#else - a two way decision also with string to int call
#x = 4
# y = input("Please enter a number between 0 and 100,")
# x = int(y)
# if x > 12 :
#     print("x is bigger than 12")
# else :
#     print("x is smaller than 12")
# print("All done!")

#More conditionals...
# y = input("Please enter a number between 0 and 11,")
# x = int(y)
# if x < 2 :
#     print("x is small")
# elif x < 10 :
#     print("x is medium")
# else :
#     print("x is large")
# print("All done")

#... Multiway
#this one has no else... what might happen?
# anum = input("Please enter a number between 0 and 11,")
# x = int(anum)
# if x < 2 :
#     print("quite small")
# elif x < 10 :
#     print("fairly medium")
# print("All done")

#...and with lots of elif but an else to catch all!
# anum = input("Please enter a number between 0 and 131,")
# x = int(anum)
# if x < 2 :
#     print("small")
# elif x < 10 :
#     print("medium")
# elif x < 20 :
#     print("larger")
# elif x < 40 :
#     print("quite big")
# elif x < 80 :
#     print("wow bigger")
# elif x < 120 :
#     print("really biggerer!")
# else :
#     print("HUGE man!")
#1:42:33

#Multiway puzzle No 1 will it print?
# anum = input("Please enter a number between 0 and 10 ish, ")
# x = int(anum)
# if x < 2 :
#     print("Below 2")
# elif x >= 2 :
#     print("Two or more")
# else :
#     print("Not sure about this one!")   #this line never prints !!
    
#Multiway puzzle No 2 will it print?
# anum = input("Please enter a number between 0 and 20 ish, ")
# x = int(anum)
# if x < 2 :
#     print("below 2")
# elif x < 20 :
#     print("below 20")
# elif x < 10 :
#     print("below 10")                      #this line never prints !!
# else :
#     print("Not sure obout this one either")

#The try / except Structure
# astr = "Hello Bob"
# try :
#     istr = int(astr)
# except :
#     istr = -1               #uses the except 
    
# print("First", istr)

# astr = '124'
# try :
#     istr = int(astr)        #doesn't need the except
# except :
#     istr = -1
    
# print("Second", istr)

#The try / except Structure - but not good with multi line block - 
# astr = 'Bob'
# try :
#     print('Hello')
#     istr = int(astr)        #blow-up
#     print('There')          #skips this line
# except:
#     istr = -1
    
# print('Done', istr)

#try / except - with user input
#1:51:01
# rawstr = input("enter a number: ")
# try :
#     ival = int(rawstr)
# except :
#     ival = -1
    
# if ival > 0 :
#     print("you're ok!")
# else :
#     print("not a number")
#1:52:40

#Ch 4 First simple function and re-use
# def thing() :
#     print("Here for...")
#     print("... fun")
    
# thing()
# print("Zippedy")
# thing()

#built-in max, min function...
#1:59:24
# big = max("Helloworld!")
# print(big)
# tiny = min("Helloworld!")   #Hello world would result in a 'blank'!
# print(tiny)
# print(big)
# print(tiny)

#built-in type conversion and controlling type (remember print()!!)
# print(float(99) / 100)

# i = 42
# type(i)

# f = float(i)
# print(f)

# type(f)

# print(1 + 2 * float(3) / 4 -5) 

#String conversion, example as try / except structure above

#Self-build functions 2:05:00