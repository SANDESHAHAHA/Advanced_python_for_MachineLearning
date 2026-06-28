# fruits = ["apple","mango","banana"]
# fruits.append("banana")
# print(fruits)
# print(fruits[0])

# tuples 

# coordinates = (12,34)
# print(coordinates[0])
# print(type(coordinates))

#sets 

# unique_members = {2,3,4,5,5,6,7,7,8} # only unique memebers are printed out 
# print(unique_members) 
# unique_members.add(88)
# print(unique_members)
# print(type(unique_members))

#dicitionaries 

# person = {
#     "name":"ram",
#     "age":23  
# }
# person["age"]=34
# person["roll"] = 35 # adding items in dict
# print(person)

# Conditional statements 

# email = input("Enter you email")
# password = input("Enter you password ")
# if email == "admin@gmail.com" and password == "password":
#     print("logged in ")
# else: 
#     print("logging failed")

#  loops 
# for i in range(5):
#     print(i)

# for _ in range(10):
#     print("Hello sandesh")

# count = 0 
# while count<5:
#     print(count)
#     count+=1

#functions 

# def fact(num):
#     f=1
#     for i in range(1,num+1):
#         f=f*i
#     return f

# print(fact(5))

# calcualte average 

# def avg(a,b,c):
#     return (a+b+c)/3

# x = int(input("Enter first: "))
# y = int(input("Enter second: "))
# z = int(input("Enter third: "))

# print(f"The average is {avg(x,y,z)}")


# classes object and  inheritance 

#make classes and make method of dogs as objects 

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name}--Woof")
    
#     def years_old(self):
#         print(f"{self.name} is {self.age} years")

# d1 = Dog("Kalu",234)
# d1.bark()
# d1.years_old()

# writing to a file 
# flag = True
# with open("example.txt","w") as f:
#     f.write("hello i am writing a line")
#     while(flag):
#         input_str = str(input("Enter the string , press n  to exit"))
#         if input_str == "n" or input_str == "N":
#             flag = False
        
#         else:
#             f.write(input_str)


# reading from a file 
# with open("example.txt","r") as f:
#     content = f.read()
#     print(content)

#exception handling 

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = num1/num2
#     print(f"The result is : {result}")

# except ZeroDivisionError:
#     print(f" {num1} can't be divided by {num2}")

# except ValueError:
#     print(f"Enter values not strings or floats")

# finally:
#     print("This block always runs ")

# Counter  : it is of colleciton module in python that is more powerful lists and dicts 

# from collections import Counter

# nums = [1,2,3,4,5,56,6,76,5,43,334]
# count = Counter(nums) # returns a dictionary 
# print(count)
# print(type(count))

# defaultdict : it a module provided by collections that created default values dynamically

# d = {}
# if "a" not in d:
#     d["a"]=d["a"]+1
# print(d["a"])

# if some values don't exist by default in dictioanry such cases must be handled manually

# from collections import defaultdict

# d = defaultdict(int)
# d["b"] = d["b"]+2
# print(d)


# dequeue  
# from collections import deque

# q = deque([2,4,5,6])
# q.appendleft(7)
# q.append(389)
# print(q)

#named tuple 

# from collections import namedtuple

# Point = namedtuple('Point','x y')
# p = Point(3,4)
# print(p)

# iterators : iterator is an method that lets you loop items one by one 
# nums = [2,3,4,5]
# it = iter(nums)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for item in nums:
#     print(item)

# nums = [12,4,5,6]
# it = iter(nums) 

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("Iteration completed")
#         break

# generator is  a simple way to build an iterator with yield , it saves memory becauses values are produced only when needed 

# def squares(n):
#     for i in range(n):
#         yield i**2

# for sq in squares(5):
#     print(sq)

#  it adds extra behaviour to a funciton with out chainging the funcion 

# def my_decorator(func):
#     def wrapper():
#         print("before function call")
#         func()
#         print("after funcion call")
#     return wrapper
        
# @my_decorator
# def sayHello():
#     print("hello brother")

# sayHello()


# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()  
#         print("Time difference:",end-start)
#         return result
#     return wrapper
# @timer
# def work():
#     for _ in range(289227):
#         pass
# work()


# funcions and lambda expresions 
# a funcion is reusable block of code that runs when you call it 
# a lambda is small, anonymous funcion

# add = lambda x,y : x+y
# print(add(3,4))

# common uses of lambda funcions : 
# sorting 

# students = [("Ram",34),("Hari",3)]
# sorted_students = sorted(students,key=lambda x:x[1])
# print(sorted_students)

#filtering

# numbers = [1,2,3,4,5,6,7,8]
# filtered_numbers = list(filter(lambda x : x%2 == 0,numbers))
# print(filtered_numbers)

# mapping 
# numbers = [i for i in range(0,11)]
# mapped_numbers = list(map(lambda x : x*x,numbers))
# print(mapped_numbers)

# oop 

# class Complex:
#     def __init__(self,real,complex):
#         self.real = real
#         self.complex = complex
    
#     def __str__(self):
#         return f"{self.real}+{self.complex}i"
    
#     def __add__(self,other):
#         r= self.real+other.real
#         i = self.complex+other.complex
#         return Complex(r,i)

# a = Complex(3,3)
# b  = Complex(2,4)
# print(a)
# print(b)

# c = a + b
# print(c)

# inheritance 

# class Animal: 
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} is speaking")
    
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed
    
#     def speak(self):
#         print(f"{self.name} is barking ")
    
# d1 = Dog("Harry","Labrador")
# d1.speak()


# debugging using pdb 

# import pdb 

# x = [1,2,3,4]  
# pdb.set_trace()

# y = x[5]

# import pdb

# def divide(a,b):
#     pdb.set_trace()
#     result = a/b
#     return result

# print(divide(10,0))


#logging  logs are better writen in file ratehr than console 

# import logging 

# logging.basicConfig(level=logging.WARNING)

# logging.info("Program started")
# logging.warning("This is  a warning")
# logging.error("This is a error ")


# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s %(message)s",
#     filename="app.log",
#     filemode="a"
# )

# logging.debug("This is debug message")
# logging.info("info")
# logging.warning("wanring")
# logging.error("error")


# from module import sum 

# print(sum(5,5))


# encapsulation along with inheritance example 


# class Patient: 
#     def __init__(self,id,age,ward):
#         self.__id = id
#         self.__age = age 
#         self.__ward = ward 
        
#     def get_patient_id(self):
#         return self.__id
    
#     def get_patient_age(self):
#         return self.__age
    
#     def get_patient_ward(self):
#         return self.__ward
    
#     def set_patient_age(self,age):
#         if age <0 or age > 130:
#             raise ValueError
#         else:
#             self.__age = age 
#     def set_ward(self,ward):
#         self.__ward = ward 
    
#     def display_info(self):
#         return f"{self.__id}-{self.__age}--{self.__ward}"
    
# class CriticalPatient(Patient):
#     def __init__(self,id,age,ward,p_level):
#         super().__init__(id,age,ward)
#         self.p_level = p_level
    
#     def display_info(self):
#         return super().display_info()


# p1 = CriticalPatient(1,123,"ICU",1)
# print(p1.display_info())


#merging dfs: inner, right , left , outer
# import pandas as pd 

# df1 = pd.DataFrame({
#     'studentId':[1,2,3],
#     'Name':['Ram','Shyam','Hari']
# })

# df2 = pd.DataFrame({
#     'studentId':[1,2,4],
#     'Name':['Ram','Shyam','Sita']
# })

# df_inner = df1.merge(df2,on='studentId')
# print(df_inner)

# df_outer = pd.merge(df1,df2,how='outer',on='studentId',suffixes=('_df1','_df2'))
# print(df_outer)

# df_left = df1.merge(df2,how='outer',on='studentId',suffixes=('_df1','_df2'))
# print(df_left)

# df_right = df1.merge(df2,how='right',on='studentId',suffixes=('_df1','_df2'))
# print(df_right)


# join combines dataframe using indexes rather column names 
# four types of join inner , outer , left and right 

# import pandas as pd 

# df_A = pd.DataFrame({
#     'Temp':[30,34,23]
# },index=['Day1','Day2','Day3'])


# df_B = pd.DataFrame({
#     'Humidity':[23,34,56]
# },index=['Day1','Day2','Day4'])

# print(df_A)
# print(df_B)

# inner_join = df_A.join(df_B,how='inner')
# print(inner_join)

# outer_join = df_A.join(df_B , how='outer')
# print(outer_join)

# left_join = df_A.join(df_B, how='left')
# print(left_join)

# right_join= df_A.join(df_B, how='right')
# print(right_join)


# example of wide format df 
# import pandas as pd 

# wide_df=pd.DataFrame({
#     'Name':['Ram','Shyam'],
#     'English':[23,45],
#     'Math':[34,45],
#     'Science':[34,23]
# })
# print(wide_df)

# long_format = pd.DataFrame({
#     'Name':['Ram','Ram','Ram','Shyam','Shyam','Shyam'],
#     'Subject':['English','Math','Science','English','Math','Science'],
#     'Marks':[23,34,34,45,45,23]
# })
# print(long_format)

# # reshaping: melt (wide to long )

# melted_df = pd.melt(
#     wide_df,
#     id_vars=['Name'],
#     var_name='Subject',
#     value_name='Score'
# )
# print(melted_df)

# # pivot: that is long format to wide format 

# pivot_df = long_format.pivot(
#     index='Name',
#     columns='Subject',
#     values='Marks'
# )
# print(pivot_df)

# # stack : converts long df in multple indexes 

# df_stacked = long_format.stack()
# print(df_stacked)


# #unstacked: unstacked is the revers of the stadck 

# df_unstacked = df_stacked.unstack()
# print(df_unstacked)

# #pivot table: advanced form of pivot and supports aggregation functions 

# long_table  = pd.DataFrame({
#     'Name':['Ram','Ram','Sita','Sita'],
#     'Subject':['Math','Math','Science','Science'],
#     'Marks':[32,54,24,32]
# })
# print(long_table)

# pivot_tbl = pd.pivot_table(
#     long_table,
#     index='Name',
#     columns='Subject',
#     values='Marks',
#     aggfunc='mean'
# )
# print(pivot_tbl)

# handling missing values

# handling categorical values 

# import pandas as pd 

# df = pd.DataFrame({
#     'Department':['HR','IT','FINANCE','DEVOPS'],
#     'Level':['Junior','Senior','Mid','Senior']
# })

# print(df.dtypes)
# print(df)

# df['Department'] = df['Department'].astype('category')
# df['Level'] = df['Level'].astype('category')

# print(df.dtypes)


# df['Level'] = df['Level'].cat.rename_categories({
#     'Junior':'Jr',
#     'Senior':'Sr',
#     'Mid':'Md'
# })

# df['Department_codes'] = df['Department'].cat.codes
# print(df)

# handling time series of sales 

# import pandas as pd 

# df = pd.DataFrame({
#     'Date':['2026-01-01','2026-01-05','2026-01-15'],
#     'Sales':[13,34,45]
# })
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.dtypes)


# date_df = pd.read_csv("dates.csv",
#                       parse_dates=["Date"],
#                       index_col="Date")

# date_df['year'] = date_df.index.year
# date_df['month'] = date_df.index.month
# date_df['day'] = date_df.index.day


# # selecting time ranges 
# print(date_df.loc["2026-01-01":"2026-01-30"])
# print(date_df.loc["2026"])
# # print(date_df)
# # print(date_df.dtypes)

