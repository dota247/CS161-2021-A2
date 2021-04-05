# Author: Juan A Wagner
# Date  : 4/01/2021
# Description: Script asks a user to enter an amount in cents less than a dollar

# this temporary value will hold the true cent amount, after floor division is done
temp = 0

print("Please enter an amount in cents less than a dollar.")

user_input = int(input())

# Using floor division you can find how many times a coin (25,10,5,1) fits evenly into the given number (user_input)
# I use temp to hold whats left and then use floor division again with the coin value i want to find.
# the value of temp will be adjusted 4 times.

quarters = user_input // 25
temp = user_input - (quarters * 25)

dimes = temp // 10
temp = temp - (dimes * 10)

nickels = temp // 5
temp = temp - (nickels * 5)

pennies = temp // 1


# Values of coins needs to be converted into string type for concatenation
print("Q: " + str(quarters))
print("D: " + str(dimes))
print("N: " + str(nickels))
print("P: " + str(pennies))








