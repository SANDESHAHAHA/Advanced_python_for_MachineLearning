# 4. Implement a function to find the factorial of a number using recursion

def fact(num):
    if num<0:
        return "undefined"
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

number=int(input("Enter a integer value: "))
print(f"The factorial is {fact(number)}")