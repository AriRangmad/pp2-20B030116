print('1')
a = 33
b = 200
if b > a:
  print("b is greater than a")


print('2')
a1 = 33
b1 = 33
if b1 > a1:
  print("b1 is greater than a1")
elif a1 == b1:
  print("a and b are equal")

print('3')
a2 = 200
b2 = 33
if b2 > a2:
  print("b is greater than a")
elif a2 == b2:
  print("a and b are equal")
else:
  print("a is greater than b")

print('4')

a3 = 200
b3 = 33
if b3 > a3:
  print("b is greater than a")
else:
  print("b is not greater than a")


print('5')
if a4 > b4: print("a is greater than b")

print('6')
a5 = 2
b5 = 330
print("A") if a5 > b5 else print("B")

print('7')
a6 = 330
b6 = 330
print("A") if a6 > b6 else print("=") if a6 == b6 else print("B")

print('8')
a7 = 200
b7 = 33
c7 = 500
if a7 > b7 and c7 > a7:
  print("Both conditions are True")

print('9')
a8 = 200
b8 = 33
c8 = 500
if a8 > b8 or a8 > c8:
  print("At least one of the conditions is True")


print('10')
a9 = 33
b9 = 200
if not a9 > b9:
  print("a is NOT greater than b")

print('11')
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

print('12')
a10 = 33
b10 = 200

if b10 > a10:
  pass