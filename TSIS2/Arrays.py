cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

cars[0] = "Toyota"

x = len(cars)

for x in cars:
  print(x)

cars.append("Honda")

cars.remove("Volvo")
cars.pop(1)

for x in cars:
  print(x)