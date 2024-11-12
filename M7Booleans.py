# Aizhamal Rysbaeva
# Nov 12, 2024

# Problem 1
# a function that takes two inputs from a user and prints whether they are equal or not.

import resources


def two_inputs():
    num1 = input("enter the first number: ")
    num2 = input("Enter the second number: ")

    if num1 == num2:
        print("the numbers are equal")
    else:
        print("the numbers are not equal")


two_inputs()


# Problem 2
# a function that takes two inputs from a user
# and prints whether the sum is greater than 10, less than 10, or equal to 10.

def compare_sum(num1, num2):
    sum = num1 + num2

    if sum > 10:
        print("the sum is greater than 10")
    elif sum < 10:
        print("sum is less than 10")
    elif sum == 10:
        print("sum is equal to 10")
    else:
        print("something went wrong")


num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))

compare_sum(num1, num2)


# Problem 3
# a function that takes a list and prints if the value 5 is in that list.

a = [6, 7, 18, 28]
i = 5

if i in a:
    print("exists")
else:
    print("doesnt exist")

# Problem 4
# a function that takes a year as a parameter
# and returns True if the year is a leap year,
# False if it is otherwise.


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


print(is_leap_year(2024))
print(is_leap_year(2020))
print(is_leap_year(1971))
print(is_leap_year(2003))

# Problem 6
# Write a function
# check whether your game character has picked up all the items needed
# perform certain tasks and checks against any weaknesses.
# Confirm checks with print statements.
# The function will take a number in as an argument.
# You can match the number to the task below.
# You don’t have to plan for inputs outside of [1,2,3].


def check_items(num):
    print(f"{resources.jama}")
    num1_weapons = ["rope", "coat", "first aid kit"]
    num2_weapons = ["pan", "groceries"]
    num3_weapons = ["pen", "paper", "idea"]
    # number has to connect to a specific list
    # print out the list conneced to the task number
    # if the number is 1, print out ["rope", "coat", "first aid kit"]
    # if the number is 2, print out ["pan", "groceries"]
    # if number is 3, print out ["pen", "paper", "idea"]
    if num == 1:
        for item in num1_weapons:
            if item in resources.jama.weapons:
                print(f"you don't have {item}")
                return False
            else:
                print("you have everythinhg you need")
        # for every item on the list i need, i want to see if it's in my weapons
        print(f"{num1_weapons}")
    elif num == 2:
        print(f"{num2_weapons}")
    elif num == 3:
        print(f"{num3_weapons}")
    else:
        print("ahahahahah")


check_items(1)
