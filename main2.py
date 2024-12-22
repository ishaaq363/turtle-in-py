import turtle

turtle.Screen().bgcolor("white")

board=turtle.Turtle()
board.fillcolor("red")
board.begin_fill()
board.forward(100)



board.left(120)
board.forward(100)

board.left(120)
board.forward(100)
board.end_fill()

board.penup()
board.fillcolor("cyan")
board.right(150)
board.forward(50)

board.pendown()
board.right(90)
board.forward(100)
board.end_fill()



turtle.done()