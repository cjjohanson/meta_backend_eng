# looping
def find_factorial_by_looping(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
            print(f"i: {i}, factorial: {factorial}")
        return factorial
    
find_factorial_by_looping(5) # 120

# recursion
def factorial_by_recursion(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial_by_recursion(n-1)

print(factorial_by_recursion(5))

def sum_by_recursion(n):
    if n == 0:
        return 0
    else:
        return n + sum_by_recursion(n-1)
    
print(sum_by_recursion(5))

def reverse_string_by_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_by_recursion(s[1:]) + s[0]