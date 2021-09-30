#Examples below taken from pythonland tutorial and copied into terminal (to run them)
#Have created file sekondeP to run example programs

# Three ways to print a string statement.
msg = "Hello to us"
print(msg)

msga= "try number 2"
print(msga)

msgb= "try number 3"
print(msgb)

#Create multi-line strings
bigmsg= """Line 1,
... Line 2, 
...Line 3."""
print(bigmsg)

#String operations
print(msgb.upper())  
      
#python functions: built in
# def say_hi():
# ...     print('Hi')
# say_hi()    

#python functions: created
def say_hi(name):
...     print('Hi', name)
...
>>> say_hi('Erik')
#Hi Erik

#Variable scope
>>> def say_yo():
...    print("Hi", name)
...    answer = "Hi"
...
>>> name = 'Erik'
>>> say_yo()
Hi Erik
>>> print(answer)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'answer' is not defined

#Default values and named parameters
>>> def welcome(name='learner', location='this tutorial'):
...     print("Hi", name, "welcome to", location)
...
>>> welcome()
Hi learner welcome to this tutorial
>>> welcome(name='John')
Hi John welcome to this tutorial
>>> welcome(location='this epic tutorial')
Hi learner welcome to this epic tutorial
>>> welcome(name='John', location='this epic tutorial')
Hi John welcome to this epic tutorial

#Booleans and operators
#Fun simple example:
>>> door_is_locked = True
>>> if door_is_locked:
...     print("Mum, open the door!")
...
Mum, open the door!
>>>

>>> door_is_locked = False
>>> if door_is_locked:
...     print("Mum, open the door!")
... else:
...     print("Let's go inside")
...
Let's go inside
>>>_

#Python For-loop
>>> for letter in 'Hello':
        ...     print(letter)
        ... 
        H
        e
        l
        l
        o

#Python for-loops and lists
>>> mylist = [1, 2, 'Hello', ['a', 'ab'] ]
>>> mylist[0]
1
>>> mylist[0] + mylist[1]
3
>>> mylist[2]
'Hello'
>>> mylist[3][0]
'a'
>>> for item in myList:
      ...     print(myList)
      ...
      
#Python While-loop
>>> i = 1
>>> while i <= 4:
...     print(i)
...     i = i + 1
... 
1
2
3
4
# press control+ c to escape infinite loops! 

#First Python Program
>>> def say_hi(name):
...     if name == '':
...         print("You didn't enter your name!")
...     else:
...         print("Hi there...")
...         for letter in name:
...             print(letter)
... 
>>> name = input()
 < enter your name at this point >
>>> say_hi(name)
#Great it worked!

#Python Comment: What It Is And How to Create
#Use self-documenting code to reduce comments to a minimum

#Docstrings: document your code with strings
#A docstring is a string that occurs as the first statement in a module, function, class, or method definition. 
#Such a docstring becomes the __doc__ special attribute of that object
#Mmm... will look at this further as tutorial progresses!

