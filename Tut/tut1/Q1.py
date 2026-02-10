# 1. Write a Python program to check if a given number is prime.

number = int(input("Enter a number: "))

def isPrime(num:int):
    flag =0 
    
    for i in range(2,num):
        if num%i == 0:
            flag=1
            break
    if flag == 1:
        return False
    else:
        return True


print(isPrime(number))
    