import turtle 
turtle.color('teal')

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

polygon(4, 100)
back(125)
polygon(3, 50)
