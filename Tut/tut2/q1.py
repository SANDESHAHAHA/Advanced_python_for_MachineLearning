# 1. Write an iterator that returns the first n even numbers.

class EvenIterator:
    def __init__(self,num):
        self.num = num
        self.current=0 
        self.count =0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count< self.num:
            self.current+=2
            self.count+=1
            return self.current
        
        else:
            raise StopIteration
        
    
  
even=EvenIterator(10)
for num in even:
    print (num)
