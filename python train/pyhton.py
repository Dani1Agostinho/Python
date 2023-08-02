from turtle import Screen, Turtle
bob = Turtle()
peter = Screen()
peter.setup(375,557)
peter.bgpic("Capture_off.GIF")


def washroom():
    bob.penup()
    bob.color("blue")
    bob.pensize(3)
    bob.setposition(85,198)
    bob.pendown()
    bob.forward(42)
    bob.left(120)
    bob.forward(42)
    bob.left(115)
    bob.forward(44)
    bob.left(120)

def Letter():
    print("Hi")

washroom()
bob.penup()
bob.setposition(0,0)
peter.mainloop()