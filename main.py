import turtle

t = turtle.Turtle()

def triagle(length, color):
  i = 0
  t.fillcolor(color)
  t.begin_fill()
  while(i <= 2):
    t.forward(length)
    t.left(120)
    i +=1
  t.end_fill()


def circle(length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.circle(int(length))
  t.end_fill()


def square(length, color):
  x = 0
  t.fillcolor(color)
  t.begin_fill()
  while(x <= 3):
    t.forward(length)
    t.right(90)
    x +=1
  t.end_fill()


def star(length, color):
  y = 0
  t.fillcolor(color)
  t.begin_fill()
  while(y <= 4):
    t.forward(length)
    t.right(36)
    t.forward(length)
    t.left(108)
    y +=1
  t.end_fill()

  
shape = input("which shape: ")
length = int(input("what length: "))
color = input("what color: ")

if(shape == "triangle"):
  triagle(length, color)
  
elif(shape == "circle"):
  circle(length, color)

elif(shape == "square"):
  square(length, color)

elif(shape == "star"):
  star(length, color)