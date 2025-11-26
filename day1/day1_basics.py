# Day 1 – Python Basics
# Author: Ankit DS
# day1_basics.py

# Variables
name = "Ankit" #String
age = 27 #int
height = 5.10 #float
message = "welcome to Next level of learning"
#Data type
print(type(height)) #to check the type of variable being stored.

# Conditional
if age >= 25:
    print(f"{height} is an adult")
else:
    print(f"{name} is a minor")

# Loop
for i in range(10):



    print(i)

# Function
def greet(person):
    return f"Hello {person}!"
def sub(subject):
    return f"welcome to {subject}!"
if age <= 25: #if want we can print with if condition too
    print(greet(name),sub(message))
# Types of operators
# Arithmetic
# +  # Addition
# -  # Subtraction
# *  # Multiplication
# /  # Division
# %  # Modulus (remainder of division)
# ** # Exponentiation (power)
# // # Floor Division (division that rounds down to the nearest whole number)
# assignment
# =   # Assigns the value on the right to the variable on the left
# +=  # Adds and assigns (e.g., x += y is equivalent to x = x + y)
# -=  # Subtracts and assigns
# *=  # Multiplies and assigns
# /=  # Divides and assigns
# %=  # Modulus and assigns
# **= # Exponentiates and assigns
# //= # Floor divides and assigns
# comparision
# == # Equal to
# != # Not equal to
# >  # Greater than
# <  # Less than
# >= # Greater than or equal to
# <= # Less than or equal to
# Logical
# and # Returns True if both statements are true
# or  # Returns True if at least one statement is true
# not # Reverses the result; returns False if the statement is true, and vice versa