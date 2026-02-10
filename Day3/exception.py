try:
    n1 = int(input("Enter a number "))
    n2 = int(input("Enter another number "))
    result = n1/n2
    print(f"Result is :{result}")
except ZeroDivisionError:
    print("You  cannot divide any number by zero ")
except ValueError:
    print("Please enter a valid number")
finally:
    print("You have successfylly run the code ")
