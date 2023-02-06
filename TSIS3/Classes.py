
class StringManipulation:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

strObj = StringManipulation()
strObj.getString()
strObj.printString()


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


class Shape:
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")

# Instantiate the class
acct1 = BankAccount('John Doe', 100)

# Make a series of deposits and withdrawals
acct1.deposit(50)s
acct1.withdraw(75)

# Test to make sure the account can't be overdrawn
acct1.withdraw(500)


nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# using filter function
prime_nums = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), nums))

print("Prime numbers in the list:", prime_nums)