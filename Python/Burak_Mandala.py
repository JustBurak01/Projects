import turtle


mandala = turtle.Turtle()
mandala.color("green")
mandala.pensize(5)
mandala.shape("square")
Hintergrund = turtle.Screen()
Hintergrund.bgcolor("black")

#Mandala
def Mandala(mandala, sz):
  for i in range(4):
    mandala.forward(sz)
    mandala.left(90)
for i in range(1,32):
  Mandala(mandala,200)
  mandala.left(18)




turtle.exitonclick()