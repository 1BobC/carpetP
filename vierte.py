#learnpython
# in file: vierte.py
# greetings = ["Hello", "Bonjour", "Hola"]

# for greeting in greetings:
#     print(f"{greeting}, World!")
   
# """
# A small Python program that uses the GitHub search API to list
# the top projects by language, based on stars.
# """

# import requests

# GITHUB_API_URL = "https://api.github.com/search/repositories"


# def create_query(languages, min_stars=50000):
#     query = f"stars:>{min_stars} "

#     for language in languages:
#         query += f"language:{language} "

#     # a sample query looks like: "stars:>50 language:python language:javascript"
#     return query


# def repos_with_most_stars(languages, sort="stars", order="desc"):
#     query = create_query(languages)
#     params = {"q": query, "sort": sort, "order": order}

#     response = requests.get(GITHUB_API_URL, params=params)
#     status_code = response.status_code

#     if status_code != 200:
#         raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
#     else:
#         response_json = response.json()
#         return response_json["items"]


# if __name__ == "__main__":
#     languages = ["python", "javascript", "ruby"]
#     results = repos_with_most_stars(languages)

#     for result in results:
#         language = result["language"]
#         stars = result["stargazers_count"]
#         name = result["name"]

#         print(f"-> {name} is a {language} repo with {stars} stars.")
        
#f-strings
#  name = "Nina"
#  greeting = f"Hello, {name}"

#  print(greeting)
#  Hello, Nina
 
 #practise basic data types
 #find types
#  x = 42
#  y = 3 / 4
#  z = int('7')
#  a = float(5)
# name = "Nina"

# #division
#  rent = 480
# >>> per_day = rent / 30
# >>> print(per_day)
# 16.0

# #three ways of printing strings
# print("Hello world")
# Hello world
# name = "Nina"
# print("My name is", name)
# My name is Nina

# name = "Nina"
# print("Hello, my name is %s" % name)
# Hello, my name is Nina
    
# name = "Nina"
# print(f"Hello, my name is {name} and I pay ${rent / 30} in rent per day")
# Hello, my name is Nina and I pay $16.0 in rent per day   

# #helper functions 
# dir()

# #functions see definitions
# # A Basic Function that accepts no arguments and returns nothing.
# def hello_world():
#     print("Hello World")
        
# # A Function that accepts two arguments, and returns the value of
# # those numbers added together.
# def mult_numbers(x, y):
#     return x * y
    
#Exercises on return statement:
#no return stmnt
#  def foo():
#      x = 5

#  val = foo()
#  type(val)
# <type 'NoneType'>

# #return stmnt no value
# def foo():
#     ...     x = 5
# ...     return
# ...
#  val = foo()
#  type(val)
# <type 'NoneType'>

# #return stmnt with value
# def oof():
#     x = 5
#     return x

# val = foo()
# type(val)
# <type 'NoneType'>

# #importance of indentation
# >>> def add_numbers(x, y):
# ... return x + y
# ...

#storing and using a return value
# >>> def add_numbers(x, y):
# ...     return x + y
# ...
# >>> new_number = add_numbers(3, 5)
# >>> new_number
# 8

# #arguements and their position
# >>> def say_greeting(name, greeting):
# ...     print(f"{greeting}, {name}.")
# ...
# >>> say_greeting("Hello!", "Nina")
# Nina, Hello!

#arguements none-default and default(keyword args)
# No default arguments
# def say_greeting(greeting, name):
#     print(f"{greeting}, {name}.")

# # Default argument - greeting will always be
# # Hello, if one isn't provided.
# def say_greeting_with_default(name, greeting="Hello", punctuation="!"):
#     print(f"{greeting}, {name}{punctuation}")

#with default arguements
# >>> def say_greeting_with_default(name, greeting="Hello", punctuation="!"):
# ...     print(f"{greeting}, {name}{punctuation}")
# ...
# >>> say_greeting_with_default("Nina")
# Hello, Nina!
# >>> say_greeting_with_default("Nina", "Good Day")
# Good Day, Nina!

#with default but wrong order!
# >>> def say_greeting_bad(greeting="Hello", name):
# ...     print("Oops, this won't work!")
# ...
#   File "<stdin>", line 1
# SyntaxError: non-default argument follows default argument

#MUST pass in all arguements 
# >>> def say_greeting(name, greeting):
# ...     print(f"{greeting}, {name}.")
# ...
# >>> say_greeting("Nina")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: say_greeting() missing 1 required positional argument: 'greeting'

#If using all default (keywords) they may or may not be passed in and if passed in can be in any order.
# >>> def create_query(language="JavaScipt", num_stars=50, sort="desc"):
# ...     return f"language:{language} num_stars:{num_stars} sort:{sort}"
# ...
# >>> create_query()
# 'language:JavaScipt num_stars:50 sort:desc'
# >>> create_query(language="Ruby")
# 'language:Ruby num_stars:50 sort:desc'
# >>> create_query(num_stars=1, language="Python", sort="asc")
# 'language:Python num_stars:1 sort:asc'

#If no defaults, keywords can be used to define args that you pass in for extra clarity
# >>> def say_greeting(name, greeting):
# ...     print(f"{greeting}, {name}.")
# ...
# >>> say_greeting("Nina", "Hello")
# Hello, Nina.
# >>> say_greeting(name="Max", greeting="Bonjour")
# Bonjour, Max.

#SCOPE (variables declared) INside a function 
# >>> def twitter_info():
# ...     twitter_account = "nnja"
# ...     print(f"Account inside function: {twitter_account}")
# ...
# >>> twitter_info()
# Account inside function: nnja
# >>> print(f"Account outside of function: {twitter_account}")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'twitter_account' is not defined

#SCOPE (variables declared) OUTside a function 
# >>> name = "Nina"
# >>> print(f"Name outside of function: {name}")
# Name outside of function: Nina
# >>>
# >>> def try_change_name():
# ...     name = "Max"
# ...     print(f"Name inside of function: {name}")
# ...
# >>> try_change_name()
# Name inside of function: Max
# >>> print(f"Name outside of function: {name}")
# Name outside of function: Nina

#SCOPE (CONSTANT variables declared)  OUTSIDE a function
# >>> ROOT_API_URL =  "https://api.github.com"  #ok to change this constant and re-call function
# >>> def api_search_repos_url():
# ...     return f"{ROOT_API_URL}/search/repositories"
# ...
# >>> api_search_repos_url()
# 'https://api.github.com/search/repositories'
# >>>

#Now for some practise starting with a basic funtion.., 
# >>> def add_numbers(x, y):
# ...     return x + y
# ... # Press Enter

# >>> add_numbers(1, 2)
# # Let's use the string formatting we learned in the last chapter
# >>> print(f"The sum of 1 and 2 is {add_numbers(1, 2)}")

#scoping..
# >>> x = 1
# >>> y = 2
# >>> def add_numbers(x, y):
# ...     print(f"Inside the function, x = {x} and y = {y}")
# ...     return x + y
# ...
# >>> print(f"Outside the function, x = {x} and y = {y}")
# >>> print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")

#Positional Arguments vs Keyword Arguments
# >>> def calculate_numbers(x, y, operation="add"):
# ...     if operation == "add":
# ...         return x + y
# ...     elif operation == "subtract":
# ...         return x - y
# ...
# # Let's try our new function. Remember, if we don't pass the operation keyword argument, the default is "add"
# >>> calculate_numbers(2, 3)
# # You can pass a keyword argument as a normal positional argument
# >>> calculate_numbers(2, 3, "subtract")
# # You can also use the argument's keyword. This helps with readability
# >>> calculate_numbers(2, 3, operation="subtract")

#Advanced data types Lists, tuples, sets, dictionaries, mutability
# >>> list()
# []
# >>> []
# []
# >>> type(list())
# <class 'list'>
# >>> type([])
# <class 'list'>

# >>> names = ["Nina", "Max", "Jane"]

# >>> len(names)
# 3

# >>> names = ["Nina", "Max", "Jane"]
# >>> names[0]
# 'Nina'
# >>> names[1]
# 'Max'
# >>> names[2]
# 'Jane'

#Indexes and Indices 
#Updating an item in a list,  Range, Formatting (actually this means layout including a trailing comma)
# >>> names = ["Nina", "Max", "Jane"]
# >>> names[2] = "Floyd"
# >>> names
# ['Nina', 'Max', 'Floyd']

#Sorting a Copy Of Your List - doesn't permanently change the list order
# >>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
# >>> sorted(lottery_numbers)
# [1, 2, 4, 11, 45, 32423]
# >>> lottery_numbers
# [1, 4, 32423, 2, 45, 11]
# >>> sorted(lottery_numbers, reverse=True)
# [32423, 45, 11, 4, 2, 1]
# >>> lottery_numbers
# [1, 4, 32423, 2, 45, 11]

#Sorting the list in-place - permanently changes the list order
# >>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
# >>> lottery_numbers.sort()
# >>> lottery_numbers
# [1, 2, 4, 11, 45, 32423]

# >>> lottery_numbers.sort(reverse=True)
# >>> lottery_numbers
# [32423, 45, 11, 4, 2, 1]

# >>> words = ["Umbrella", "Fox", "Apple"]
# >>> words.sort()
# >>> words
# ['Apple', 'Fox', 'Umbrella']

#Reverse the list in-place. Uses reverse() method. Different to reverse=True
# >>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
# >>> lottery_numbers.reverse()
# >>> lottery_numbers
# [11, 45, 2, 32423, 4, 1]

#Finding Methods eg:
#dir(list)

#lists 2, (Looking for items more quickly use set or dic - later)
# names = ["Nina", "Max", "Phillip", "Nina"]
# >>> "Nina" in names
# True
# >>> "Rose" in names
# False

#Adding items
# >>> names.append("John")
# >>> names
# ['Nina', 'Max', 'John']

# >>> names.insert(0, "Rose")
# >>> names
# ['Rose', 'Nina', 'Max', 'John']

# #getting help
# >>> type(names)
# <class 'list'>
# >>> help(names.insert)

# Help on method_descriptor:

# insert(self, index, object, /)
#     Insert object before index.

# #adding a list to a list
# >>> names = ["Nina", "Max"]
# >>> colors = ["Red", "Blue"]
# >>> names
# ['Nina', 'Max']
# >>> names.extend(colors)
# >>> names
# ['Nina', 'Max', 'Red', 'Blue']

#Looking for Items - True / False above but also...
#with error or with count
# >>> names.index("Nina")
# 0
# >>> names.index("Rose")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 'Rose' is not in list

# >>> names.count("Nina")
# 2
# >>> names.count("Rose")
# 0

#Updating Items
# >>> names = ["Nina", "Max"]
# >>> names[0] = "Rose"
# >>> names
# ['Rose', 'Max']

# #Take a moment to look carefully at this one!
# >>> names = ["Nina", "Max"]
# >>> pos = names.index("Max")
# >>> names[pos] = "Rose"
# >>> names
# ['Nina', 'Rose']






