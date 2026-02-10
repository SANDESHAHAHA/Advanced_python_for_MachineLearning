#15. Implement a Python function that generates the Fibonacci sequence up to n terms

def fibonacci(n):
    
    if n==0:
        return []
    if n==1:
        return [0]
    fibo_series=[0,1]
    
    while len(fibo_series)<n:
        next_term=fibo_series[-1]+fibo_series[-2]
        fibo_series.append(next_term)
    
    
    return fibo_series

term=int(input("Enter the number to generate fibonacci series: "))
print(f"The series is : {fibonacci(term)}")