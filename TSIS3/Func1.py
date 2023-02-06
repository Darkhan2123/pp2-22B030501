import math
import random
def conv(grams):
    ounces = 28.3495231 * grams
    return ounces

def temp(Fahrenheit):
    f = int(input())
    c = (5 / 9) * (f - 32)
    return c


def solve(numheads, numlegs):
    numchickens = (4*numheads - numlegs)//2
    numrabbits = numheads - numchickens
    return (numchickens, numrabbits)

print(solve(35, 94))

def filter_prime(numbers):
  prime_numbers = []
  for num in numbers:
    if is_prime(num):
      prime_numbers.append(num)
  return prime_numbers

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

x = [3, 5, 6, 7, 9, 17]
print(filter_prime(x))

def toString(List):
    return ''.join(List)
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)

            # backtrack
            a[l], a[i] = a[i], a[l]


# Driver code
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)

def reverses(string):
    return string[::-1]

a = ["We", "are", "ready"]

print(reverses(a))

def has_33(nums):
    if "33" in nums:
        return "True"
    return "False"
number = 1444325533
number = str(number)
print(has_33(number))

def spy_game(nums):
    if "007" in nums:
        return True
    return False
number = 12400775
number = str(number)
print(spy_game(number))

#or U can do like this

def contains_007(nums):
  for i in range(len(nums)-2):
    if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
      return True
  return False

def volume_of_a_sphere(radius):
    Volume = (4 * math.pi * radius**3) / 3
    return Volume

print(volume_of_a_sphere(5))

def unique(List):
    unique_list = []
    for x in List:
        if x not in unique_list:
            unique_list.append(x)

    for x in unique_list:
        print(x, end=" ")
List = [10,10, 20, 31, 20]
unique(List)

def is_it_palindrome(string):
    original_string = string
    string = string[::-1]
    if string == original_string:
        return True
    return False
string = "mad"
print(is_it_palindrome(string))

def histogram(List):
    for i in List:
        for j in range(i):
            print('*', end ="")
        print()

list1 = [4, 9, 7]
histogram(list1)

# Number between 1 to 20
n = random.randint(1, 20)
answer = n
print("Hello! What's your name? ", end="")
s = input()
print(s)

print("Well, {zzxc}, I am thinking of a number between 1 and 20.".format(zzxc = s))

print(number)
counter = 0
while number != answer:
    print("Take a guess.")
    number = int(input())
    if(number > answer):
        print("Your guess is too big")
    else:
        print("Your guess is too low.")
    counter += 1
print("Good job, KBTU! You guessed my number in {res} guesses!".format(res = counter))