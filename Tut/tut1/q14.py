#14. Write a function to reverse a list without using the built-in reverse() method.

def Reverse(lst):
    new_list=lst[::-1]
    return new_list
print(f"The reversed string is: {Reverse([3,4,2,5,6])}")
    
    
    