#20. Create a function that calculates the sum of digits of a given number

def sum_of_digits(num):
    sum=0
    while num>0:
        digit =num%10
        num = num//10
        sum= sum + digit
   
    return sum 
        


print(sum_of_digits(123))