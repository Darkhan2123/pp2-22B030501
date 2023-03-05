#1
from functools import reduce

def multiply_list(lst):
    product = reduce((lambda x, y: x * y), lst)
    return product

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print(result)  # Output: 120

#2
def count_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

# Example usage:
string = "Hello, World!"
upper, lower = count_letters(string)
print("Number of uppercase letters:", upper)  # Output: 2
print("Number of lowercase letters:", lower)  # Output: 10

#3
def is_palindrome(s):
    return s == s[::-1]

# Example usage:
string = "racecar"
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")  # Output: racecar is a palindrome

#4
import time
import math

def square_root_with_delay(num, delay):
    time.sleep(delay / 1000)
    result = math.sqrt(num)
    return result

# Example usage:
number = 25100
delay = 2123
result = square_root_with_delay(number, delay)
print("Square root of", number, "after", delay, "milliseconds is", result)
# Output: Square root of 25100 after 2123 milliseconds is 158.42979517754858

#5

def all_true(t):
    return all(t)

# Example usage:
t1 = (True, True, False)
t2 = (1, "hello", [1, 2, 3])
t3 = (True, 1, [1, 2, 3])
print(all_true(t1))  # Output: False
print(all_true(t2))  # Output: True
print(all_true(t3))  # Output: True
