# Topic covered
# - Concatenation
# - Type Casting
# - input()
# - eval() 

# ? Concatenation - use to merge two or more strings
# example
str1 = "Hello"
str2 = "Universe"
newStr = str1 + str2
print("1.", newStr)

# ? Type casting - coversion of data from one datatype to another datatype
# ? Two types of type casting - 1. implicit 2. ExplicitN
str1 = "12"
print(type(int(str1)))

# ? input - use to take input from the user of enter manuall data 
# ! Entered datatype is always a string by default wheather you pass number or charater
userName = input("Enter your name: ")
userAge = input("Enter your age: ")
print("Your name: ", userName)
print("Your age: ", userAge)

# ? eval() - In case given number is passed as string it take it and give output in integer
num_1 = input("Enter the num 1: ")
num_2 = input("Enter the num 2: ")
operator = input("What operation do you want to perform? \n (+, -, *, /, //, **, %): ")
result = print("Result is: ", eval(f"{num_1} {operator} {num_2}"))