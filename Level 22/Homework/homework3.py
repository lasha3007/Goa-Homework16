def num_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

print(num_divisors(20))  
