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
smallest = None
print("Before")
for value in [20, 19, 21, 18, 22, 17, 23, 16, 1000, 24, 15, 25] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)          #YEAH - indentation!!!
print("After ", smallest)