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
 x = 42
 y = 3 / 4
 z = int('7')
 a = float(5)
name = "Nina"

#division
 rent = 480
>>> per_day = rent / 30
>>> print(per_day)
16.0

#three ways of printing strings
print("Hello world")
Hello world
name = "Nina"
print("My name is", name)
My name is Nina

name = "Nina"
print("Hello, my name is %s" % name)
Hello, my name is Nina
    
name = "Nina"
print(f"Hello, my name is {name} and I pay ${rent / 30} in rent per day")
Hello, my name is Nina and I pay $16.0 in rent per day   

#helper functions 
dir()

#functions see definitions
