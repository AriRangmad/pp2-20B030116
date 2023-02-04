print('1')
thistuple = ("apple", "banana", "cherry")
print(thistuple)


print('2')
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


print('3')
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


print('4')
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


print('5')
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


print('7')
tuple1 = ("abc", 34, True, 40, "male")


print('8')
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print('9')
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)