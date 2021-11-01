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
county = 0
summer = 0
print("Before", county, summer)
for valve in [18, 32, 57, 9, 3, 89, 107, 203] :
    county = county + 1
    summer = summer + valve
    print("iteration:", county,"running total:", summer, "array value:", valve, "running average :", summer / county)
print("After", county, summer, "final average:", summer / county)

#2:44:35 Filtering in loops