price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# we can turn it into a number with two decimal to do that we write like this

txt = "The price is {:.2f} dollars"

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))