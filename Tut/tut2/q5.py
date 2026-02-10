# . Implement an iterator class that iterates over a range in reverse order

class revRange:
    def __init__ (self,start,end):
        self.start = start 
        self.current = end-1
        
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>=self.start:
            value = self.current
            self.current-=1
            return value 
        else:
            raise StopIteration
for num in revRange(1,6):
    print(num)
            