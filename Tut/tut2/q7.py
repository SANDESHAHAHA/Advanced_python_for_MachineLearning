# 7. Create a decorator to measure memory usage of a function.

import tracemalloc

def measure_memory(func):
    def wrapper(*args,**kwargs):
        tracemalloc.start()
        result = func(*args,**kwargs)
        current,peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"[{func.__name__}] "
              f"Current memory: {current/1024:.2f} KB |"  f"Peak Memory: {peak / 1024:.2f}KB"
              )
        return result
    return wrapper

@measure_memory
def create_list():
    data= [i for i in range(100000)]
    del data


create_list()