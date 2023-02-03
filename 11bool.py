print('1')
print(10 > 9)
print(10 == 9)
print(10 < 9)

print('2')
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print('3')
print(bool("Hello"))
print(bool(15))

print('4')
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print('5')
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

print('6')
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


print('7')
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print('8')
def myFunction() :
  return True

print(myFunction())

print('9')
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

print('10')
x = 200
print(isinstance(x, int))