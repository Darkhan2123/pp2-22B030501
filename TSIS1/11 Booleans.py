# True or false

print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

# Another example where we print text instead of T and F

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello")) #True
print(bool(15)) #True
print(bool(0)) #False

'''
All of this will give u false 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

#Don't know about the classes so no comments
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))