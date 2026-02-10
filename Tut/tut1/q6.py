#6. Create a function that takes a list of numbers and returns only the even numbers.

def even_numbers(lst):
    even=filter(lambda x: x%2==0,lst)
    print(type(even))
    return list(even)
lst=[2,5,7,6,9]
print(f"Even : {even_numbers(lst)}")