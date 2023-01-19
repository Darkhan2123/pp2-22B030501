print("Hello")
print('Hello')

#The same thing

a = "Hello"
print(a)

#Also u can do like this

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#printing first character of the string

a = "Hello, World!"
print(a[0])

#printing by column

for x in "banana":
  print(x)

#length of the string

a = "Hello, World!"
print(len(a))

#searching sentence from a set of sentences

txt = "The best things in life are free!"
print("free" in txt)

##Printing only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Also you can check it by "not in"

txt = "The best things in life are free!"
print("expensive" not in txt)