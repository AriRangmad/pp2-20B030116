print('2')
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


print('3')
i1 = 0
while i1 < 6:
  i1 += 1
  if i1 == 3:
    continue
  print(i1)

print('4')
i2 = 1
while i2 < 6:
  print(i2)
  i2 += 1
else:
  print("i is no longer less than 6")