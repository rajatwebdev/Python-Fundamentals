#Self keyword is mandatory for calling variable names into methods.
#Instance and class variables have whole different purpose.
#Constructor name should be __init__.
#New keyword is not required when you create object.
#Classes are user defined blueprint or prototype.

class calculator:
    num = 100 # -> Class Verible because it is inside of class.

    #Default Constructor
    def __init__(self, apple, ball): # -> Constructor
        self.apple = apple
        self.ball = ball
        print("I get called automatically when object is created")

    def getData(self):  # -> Function
        print("Start Calculating....")

    def summation(self):
        return self.apple + self.ball + calculator.num


obj = calculator(11, 6)
obj.getData()
print(obj.summation())
