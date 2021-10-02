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
# Nina, Hello!.def

#arguements none-default and default(keyword args)
# No default arguments
def say_greeting(greeting, name):
    print(f"{greeting}, {name}.")

# Default argument - greeting will always be
# Hello, if one isn't provided.
def say_greeting_with_default(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")