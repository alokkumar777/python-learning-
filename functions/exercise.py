# Exercise level-3
# Write a function called is_prime, which checks if a number is prime.

def isPrime(num: int) -> str:
    return [
        "Prime" if num % i != 0 else "Not Prime" 
        for i in range(2, int(num ** 0.5) + 1)
        ]
        
# print(isPrime(8))

def checkUnique(lst: list) -> bool:
    return len(lst) == len(set(lst))

lst = [1, 2, 3, 4, 4]
# print(checkUnique(lst))

def allSameType(lst) -> bool:
    if not lst:
        return  True
    first_type = type(lst[0])
    return all(isinstance(i, first_type) for i in lst)

print(allSameType([1, 2, 5]))
    

