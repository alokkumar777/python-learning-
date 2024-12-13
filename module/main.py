import string
import random

def randomUserID(length, times):
    characters = string.ascii_letters + string.digits
    random_ids = [
        "".join(random.choices(characters, k=length)) 
        for _ in range(times)
    ]
    return random_ids

# Example usage
length = int(input("Length: "))
times = int(input("Times: "))
print(randomUserID(length, times))



