import turtle


def draw_diamond(some_turtle):

    for i in range(1, 4):
        ##chip = turtle.Turtle()
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(30)


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("yellow")
    charlie = turtle.Turtle()
    charlie.shape("turtle")
    charlie.color("red")
    charlie.speed(5)
    for i in range(1, 19):
        draw_diamond(charlie)
        charlie.right(10)


draw_flower()
