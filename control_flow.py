# -*- coding: utf-8 -*-
"""Control Flow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bPNcGCTwtzb4J07QIdICP7j_wwO6Ke6E
"""

# If Statement

number = 20
if (number < 15):
    print("Number  is smaller than 15")
    print("I'm in if Block")
else:
    print("Number  is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")

i = 10
print(True) if i < 12 else print(False)

# checking for odd or even numbers
number = int(input("Give a random number \n"))

if number % 2 == 0:
  print("The number is even")
else:
    print("The number is odd")

letter ="A"

if letter == "B":
    print("letter is B")



elif letter == "C":
    print("letter is C")


elif letter == "A":
    print("letter is A")

else:
    print("letter isn't A, B and C")

# check odd or even number using lambda function
number = lambda x : f"{x} is a even number" if x % 2 == 0 else f"{x} is a odd number"
print(number(22))
print(number(13))

# multiple conditions using lambda
number = lambda x,y : f"{x} is smaller than {y}." \
if x < y else (f"{x} is greater than {y}." if x > y \
               else f"{x} is equal to {y}.")
print(number(11,13))
print(number(23,18))
print(number(11,11))

# eligibility to vote
age = int(input("Enter your age: "))

if age >= 18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")