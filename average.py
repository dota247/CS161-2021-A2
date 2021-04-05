# Author: Juan A Wagner
# Date  : 4/01/2021
# Description: A program that takes 5 inputs from the user and finds the average

# need to initialize temp variable for summation, otherwise the first addition will not be uniform.
temp = 0

print("Please enter 5 numbers.")

# asks the user for 5 numbers, adding them one by one
user_data = input()
temp = temp + float(user_data)

user_data = input()
temp = temp + float(user_data)

user_data = input()
temp = temp + float(user_data)

user_data = input()
temp = temp + float(user_data)

user_data = input()
temp = temp + float(user_data)

#calculates the average of the collected values

average = temp/5

# returns the average with a message for the user
print("The average of those numbers is:")
print(average)
