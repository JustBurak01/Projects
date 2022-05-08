import turtle


Leonardo = turtle.Turtle()
Leonardo.color("green")
Leonardo.pensize(5)
Leonardo.shape("turtle")
Hintergrund=turtle.Screen()
Hintergrund.bgcolor("black")
#A
Leonardo.right(60)
Leonardo.forward(200)
Leonardo.backward(200)

Leonardo.left(-60)
Leonardo.forward(200)
Leonardo.backward(85)

Leonardo.left(120)
Leonardo.forward(112)
Leonardo.penup()
Leonardo.forward(80)
Leonardo.pendown()


#D
Leonardo.circle(90, 180)
Leonardo.left(90)
Leonardo.forward(180)

Leonardo.penup()
Leonardo.left(90)
Leonardo.forward(150)
Leonardo.pendown()

#A
Leonardo.right(60)
Leonardo.forward(200)
Leonardo.backward(200)

Leonardo.left(-60)
Leonardo.forward(200)
Leonardo.backward(85)

Leonardo.left(120)
Leonardo.forward(112)
Leonardo.penup()
Leonardo.forward(80)
Leonardo.pendown()

def quadrat():
    Leonardo.penup()
    Leonardo.goto(-350, 100)
    Leonardo.pendown()
    Leonardo.forward(100)
    Leonardo.left(90)
    Leonardo.forward(100)
    Leonardo.left(90)
    Leonardo.forward(100)
    Leonardo.left(90)
    Leonardo.forward(100)
    Leonardo.left(90)

quadrat()

turtle.exitonclick()



