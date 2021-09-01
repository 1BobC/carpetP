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
print(msgb.upper()   
      
#python functions: built in
def say_hi():
...     print('Hi')
say_hi()    

#python functions: created
>>> def say_hi(name):
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