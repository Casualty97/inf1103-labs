
# Activity 1
print("===================================")
print("Welcome here")
print("My first post!")
print("===================================")

# a. Does the program display messages exactly as written? 
# Yes

# b. Order of execution - top to bottom, or bottom to top? 
# Top to bottom

# c. Where does the output appear? 
# in Terminal

# Activity 2
username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

# a. What is the use of the variables "username", "bio" and "followers"? 
# They store assigned values

# b. If you change these values, does the output change? 
# Yes, the output will change to reflect the new values

# Activity 3
followers = 100

followers += 50
print("Day 1:", followers)

followers += 20
print("Day 2:", followers)

followers -= 10
print("Day 3:", followers)

# a. Do we manually have to reassign the follower value? 
# No

# b. Does each operation affect the first value (100) or the existing
#     value of followers? 
# It affects the existing value of followers

# c. What is the use of the += and -= operators? 
# The += operator adds a value to the existing variable, while the -= operator subtracts a value from the existing variable.

# Activity 4
# username = input("Enter Username: ")
# age = input("Enter Age: ")
# category = input("Enter Content Category: ")

# print("\nInstagram Profile")
# print("====================")
# print("Username:", username)
# print("Age:", age)
# print("Category:", category)

# a. How does input() capture what the user types?
# The input() function waits for the user to type something and press Enter, then it captures that input as a string.

# b. Is the program dynamic now, or still hard coded?
# The program is dynamic now because it takes user input instead of using hard-coded values.

# c. Try running it several times with different inputs.
# Yes, running the program multiple times with different inputs will yield different outputs based on what the user enters.

# Activity 5

username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("====================")
print("Username:", username)
print("Age:", age)
print("Category:", category)

if age>40 and category == "fun":
    print("You are old what is fun for you??")

# a. What is the return type of input()?
# The return type of input() is a string.

# b. How are the different conditions being checked?
# The conditions are checks using 'if', where if the age is greater than 40 and the category is "fun", 
# it will print a specific message.