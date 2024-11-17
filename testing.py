# perfect number or not

def check_perfect_or_not(user_input):
    sum_of_divisor = 1
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            sum_of_divisor += i
            if i != user_input // i:
                sum_of_divisor += user_input // i
            
    if sum_of_divisor == user_input:
        return f"{user_input} is Perfect Number"
    else:
        return f"{user_input} is Not perfect"

user_input = 28
print(check_perfect_or_not(user_input))