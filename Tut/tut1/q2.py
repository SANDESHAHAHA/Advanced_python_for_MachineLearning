# Create a function that converts a list of temperatures from Celsius to Fahrenheit.


temp=float(input("Enter temperature in celcius: "))

def celcius_to_F(c):
    f=(9/5*c)+32
    return f

print(f"The {temp} degree celcius is equivalent to {celcius_to_F(temp)} deg Fahrenheit ")