#17. Create a function that accepts a variable number of arguments and returns their sum.

def addition(*args):
    
    sum=0
    for item in args:
        sum = sum + item 
    return sum 

aTuple=(1,2,3,4,5)
print(f"Sum of variable arguments: {addition(*aTuple)}")  # sending variable tuples data by unpacking 