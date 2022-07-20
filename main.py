x = input("enter first name: ")
y = input("enter last name: ")


def addNames(name1, name2):
    return (name2 + name1)


if (y=="bond"):
  print("hello, 007")
else:
  print(f"hello, {addNames(x , y )}")



