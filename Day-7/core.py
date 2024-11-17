# Topic covered
# Operators
    # Arithmetic
        # Addition +
        # Subtraction - 
        # Division / 
        # Multipication *
        # Floor Division // 
        # Modules Or Reminder %
        # Power **

    # Comparision - Take data in (int, str, float) give output in (True or False)
        # Less than <
        # Greater than >
        # Less than equal to <=
        # Greater than equal to >=
        # Equal to ==
        # Not equal to !=

    # Logical 
        # and
        # or
        # not
    
# ! Single line if-else
# * SYNTAX: True_block if condition_block else False_block

# Practice Questions on Logical Operators
age = 23
height = 130
is_student = True

if age >= 18 and height >= 160 and is_student == True:
    print("You are eligible to ride a roller coaster") 
else:
    print("You are not eligible")   

# Another question
def should_stay_home(is_weekend, is_holiday, is_raining):
    if is_holiday or (is_weekend and is_raining):
        print ("Person stay at home")
    else:
        print ("Person go out")

should_stay_home(1, 0, 0)

# Another one
A = 0
B = 1
C = 0
if A or B or C:
    print("True")
else:
    print("False")