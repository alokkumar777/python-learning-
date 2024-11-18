# Exercise level-3
# Write a function called is_prime, which checks if a number is prime.

def isPrime(num: int) -> bool:
    return [
        "Prime" if num % i != 0 else "Not Prime" 
        for i in range(2, int(num ** 0.5) + 1)
        ]
        
print(isPrime(8))


