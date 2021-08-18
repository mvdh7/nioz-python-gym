"""Boolean logic"""
from setup_boolean_logic import temperature, salinity, x, y
import check_boolean_logic as check

#%% Part 0: basic functions
# Exercise 0
def func0(x, y):
    """Add x and y together."""
    # write any intermediate code you need here
    return  # write your function output here


test0 = func0(x, y)  # use this to test your function as you build it
# check.ex0(func0)  # run this to check if your function works correctly at the end

#%% Part 1: arrays of numbers
# Exercise 1:
def func1(temperature):
    """Return an array that is True where the input array (i.e. temperature)
    is greater than 18.
    """
    return


test1 = func1(temperature)
# check.ex1(func1)

#%% Exercise 3:
# # Create an array that is True where temperature is greater than 18.
# answer3 = temperature > 18
# check.ex3(answer3)

# # Exercise 4:
# # Create an array that is True where temperature is greater than 18, and less than
# # or equal to 21.
# answer4 = (temperature > 18) & (temperature <= 21)
# check.ex4(answer4)

# # Exercise 5:
# # Create an array that is True where temperature is less than or equal to 18, or
# # more than 21.
# answer5 = (temperature <= 18) | (temperature > 21)
# check.ex5(answer5)

# # Exercise 6:
# # Create an array that is True where temperature is in the ranges specified in
# # Ex. 5, and salinity is less than or equal to 35.
# answer6 = answer5 & (salinity <= 35)
# check.ex6(answer6)

# # Exercise 7:
# # Create an array that is True where temperature is exactly 21 or salinity is
# # exactly 35.
# answer7 = (temperature == 21) | (salinity == 35)
# check.ex7(answer7)

# #%% Part 2: arrays to single values
# # For exercises 8 to 11, write a function that returns a single True or False value
# # or a number (as appropriate), that shows...


# # Exercise 10:
# # ... if there are any points where temperature is less than 4 and salinity is
# # greater than 40?
# answer10 = any((temperature < 4) & (salinity > 40))
# check.ex10(answer10)

# # Exercise 11:
# # ... how many points are there with temperature is less than 4 and salinity is
# # greater than 40?
# answer11 = sum((temperature < 4) & (salinity > 40))

# # Exercise 12:
# # ... if all the points with temperature less than 4 also have a salinity
# # greater than 40?
# tg = temperature < 4
# sg = salinity > 40
# answer12 = all((tg & sg) | ~tg)

# # Exercise 13
# # ... if all the points with temperature less than 8 also have a salinity
# # greater than 40?
# tg = temperature < 8
# sg = salinity > 40
# answer13 = all((tg & sg) | ~tg)
