# binary search
import time

def binary_search(arr, target):
    loop_counter = 1
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"low: {low}, high: {high}, mid: {mid}")
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid, loop_counter
        loop_counter += 1
        
    return -1, loop_counter

arr = range(1, 10000)
target = 3
print(binary_search(arr, target))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(3))
