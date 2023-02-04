print('1')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('2')
for x in "banana":
  print(x)

print('3')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


print('4')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


print('5')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print('6')
for x in range(6):
  print(x)


print('7')

for x in range(2, 6):
  print(x)


print('8')
for x in range(2, 30, 3):
  print(x)


print('9')
for x in range(6):
  print(x)
else:
  print("Finally finished!")


print('10')
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


print('11')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


print('12')
for x in [0, 1, 2]:
  pass