#Not sure yet how I'll use this!
#Oh, now I know!

#print('Hello, World!')

#Classes and Objects in Python
#len(5)  #see error

#What are Python Methods?
#dir(5)
#dir("test")

#What are classes and objects in Python?
#Creating classes and objects in Python
#What Is self in Python?
class Car:
    speed = 0
    started = False
 
    def start(self):
        self.started = True
        print("Car started, let's ride!")
 
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")
 
    def stop(self):
        self.speed = 0
        print('Halting')
  
#Creating Multiple Objects      
>>> car1 = Car()
>>> car2 = Car()
>>> id(car1)
139771129539104
>>> id(car2)
139771129539160

>>> car1.start()
Car started, let's ride!
>>> car1.increase_speed(10)
'Vrooom!'
>>> car1.speed
10
>>> car2.speed
0

#Python Constructors see index html
class Car:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("Car started, let's ride!")
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start the car first")
    def stop(self):
        self.speed = 0
        
#Python Inheritance
