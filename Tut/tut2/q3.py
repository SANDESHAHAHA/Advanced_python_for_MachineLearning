# 3. Implement a decorator that prints “Start” before a function and “End” after it

def myDecorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@myDecorator
def sayHello():
    print("Hello")

sayHello()