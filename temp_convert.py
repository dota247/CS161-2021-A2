# Author: Juan A Wagner
# Date  : 4/01/2021
# Description: The program takes in a temperature value, this value is converted into Fahrenheit.

# records user input to be converted
celsius = input("Please enter a celsius temperature:")

# The users' input is type casted to float then plugged into [(9/5) * C + 32], where C is the user's input.
fahrenheit = (9/5) * float(celsius) + 32

# Returns results of conversion with a message
print("The equivalent Fahrenheit temperature is: ")
print(fahrenheit)



