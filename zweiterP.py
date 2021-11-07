#This file will be re-used for python programs from Code-camp Python for Everybody 
#moving from file ersterP 
#More Loop Patterns
#Counting in a loop 2:40:00
# zork = 0
# print("zork, Before: ", zork)
# for thing in [18, 32, 57, 9, 3, 89, 107, 203] :
#     zork = zork + 1
#     print("zork", zork, "thing", thing)
# print("zork, After: ", zork)

#Summing in a loop
# zork = 0                                            #the sum variable
# print("zork, Before: ", zork)
# for thing in [18, 32, 57, 9, 3, 89, 107, 203] :
#     zork = zork + thing                             #add thing variable to zork for running total
#     print("zork", zork, "thing", thing)
# print("zork, After: ", zork)

#Finding the average
# county = 0
# summer = 0
# print("Before", county, summer)
# for valve in [18, 32, 57, 9, 3, 89, 107, 203] :
#     county = county + 1
#     summer = summer + valve
#     print("iteration:", county,"running total:", summer, "array value:", valve, "running average :", summer / county)
# print("After", county, summer, "final average:", summer / county)

#2:44:35 Filtering loops with an if statement
# print("Before")
# for value in [20, 19, 21, 18, 22, 17, 23, 16, 24, 15, 25] :
#     print("The array value: ", value)
#     if value > 20 :
#         print("Filtered value: ", value)
# print("After")

#Search in loops with a Boolean statement
# found = False
# print("Before", found)
# for value in [20, 19, 21, 18, 22, 17, 23, 16, 1000, 24, 15, 25] :
#     if value == 1000 :
#         found = True
#     print(found, value)
# print("After", found)

#continue at 2:50:00
#Discussion on finding smallest number introduces the use of None and is
# smallest = None                   #could be used in finding largest number
# print("Before")
# for value in [20, 19, 21, 18, 22, 17, 23, 16, 1000, 24, 15, 25] :
#     if smallest is None :
#         smallest = value
#     elif value < smallest :
#         smallest = value
#     print(smallest, value)          #YEAH - indentation!!!
# print("After ", smallest)

#Ch 6 Strings 2:59:00
#Using terminal - Looking inside strings - Looping through Strings
# fruit = "banana"
# index = 0
# while index < len(fruit) :
#     letter = fruit[index]
#     print(index, letter)
#     index = index + 1

#doing the same job but with a for statement - tres elegant! - see the difference?
# fruit = 'banana'
# for letter in fruit :
#     print(letter)

#Looping and counting
# word = 'banana'
# count = 0
# for letter in word :
#     if letter == 'a' :
#         count = count + 1
# print(letter, count)

#More about in 3:07:36      in is great!
# for letter in 'banana' :
#     print(letter)
    
#More things with strings
#Slicing
# s = 'Monty Python'
# print(s[0:4])
# print(s[6:7])
# print(s[0:5])
# print(s[6:20])        #works to the end of the string 3:11:42

#plus variations on what can be ommitted [:2] etc.

#normal string concatanation does not create spaces, you have to add +" "+s

#in can be used as a logical operator which can be used in an if statement
# fruit = "banana"
# print('n' in fruit)
# print('m' in fruit)
# print('nan' in fruit )  
# if 'a' in fruit :
#     print("Found it")
#Mmm...geting lost but OK now, proceed from 3:13:34 

#String comparison - clever illustration
word = input("Please enter the name of a fruit (hint - banana!")
if word == "banana" :
    print("All right, bananas.")

if word < "banana" :
    print("Your word," + word + ", comes before banana.")
elif word > "banana" :
    print("your word," + word + ", comes after banana.")
else :
    print("All right, bananas.")

#String library start 3:15:28