# 8. Write a generator that yields prime numbers indefinitely 

def genPrime(func):
    def wrapper():
        print("started generation prime ")
        func()
        print("hi")
    return wrapper
@genPrime
def createPrme():
    while True:
        num = 2
        
        
    
