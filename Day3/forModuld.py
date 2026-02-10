#method 1
# from module  import simpleInterest,cInterest  # Note that main functino isnot invoked in other functions 
#mehtod 2
from Day3.module import *
#method 3 
import Day3.module as m
p=100
t=2
r=24
print(f"Simple Intersst:{m.simpleInterest(p,t,r)}")