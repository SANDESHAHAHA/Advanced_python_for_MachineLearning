# 2. Write a generator that yields the Fibonacci sequence up to n terms

def fibonacci(n):
    
    if n ==0:
        yield []
    if n==1:
        yield [0]
    
    fibo_series =[0,1]
    
    while len(fibo_series)<n:
        next_term = fibo_series[-1]+fibo_series[-2]
        fibo_series.append(next_term)
    yield fibo_series

num = int(input("Enter the number of terms to generate fibonacci !: "))
result = fibonacci(num)
print(result)
for item in result:
    print(item)