import turtle

class MyTurtle(turtle.Turtle):
    """
    Initiates an instance object Turtle and creates a class of usable turtle
    slaves
    """
D = 90 #Turning Angle
L = 10 #Line Length

    def iterate(axiom, num=0, initator='F'):
        """
        Compute turtle rule string by iterating on an axiom
        """

        def translate(current, axiom):
            """
            Translate all the "F" with the axiom for current string
            """
            result = ""
            consts = {'+', '-', '[', ']'}
            for c in current:
                if c in consts:
                    result += c
                    continue
                    if c == 'F':
                        result += axiom
            return result

            # Sets initator
            result = initator
            for i in xrange(0, num): # Translates the rule string for each iteration
                result = translate(result, axiom)
            return result

def draw(axiom, d=D, l=L):
    """
    Uses turtle to draw the L-System
    """
    stack  = []                 # Tracks the turtle's position
    screen = turtle.Screen()
    Jonathan = turtle.Turtle()
    Jonathan.hideturtle()           # Doesn't show the turtle
    Jonathan.speed("faster")
    Jonathan.left(90)               # Points upwards instead of rightwards

    for i in xrange(len(axiom)):
        c = axiom[i]

        if c == 'F':
            Jonathan.forward(l)

        if c == 'f':
            Jonathan.penup()
            Jonathan.forward(l)
            Jonathan.pendown()

        if c == '+':
            Jonathan.left(d)

        if c == '-':
            Jonathan.right(d)

        if c == '[':
            stack.append((Jonathan.heading(), Jonathan.pos()))

        if c == ']':
            heading, position = stack.pop()
            Jonathan.penup()
            Jonathan.goto(position)
            Jonathan.setheading(heading)
            Jonathan.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    turtle.mainloop()

    """
    For a Koch Fractal:
    axiom = "F+F--F+F"
    axiom = iterate(axiom, 3, "F")
    draw(axiom, 60, 10)
    For Other fractal:
    axiom = "F[-F]F[+F]F"
    axiom = iterate(axiom, 3, "F")
    draw(axiom, 60, 10)
    """

    def glow(self,x,y):
        self.fillcolor("red")

    def unglow(self,x,y):
        self.fillcolor("")

    def koch(order, size):
        #must be 5 < order < 1
        window = turtle.Screen()
        t = turtle.Turtle()
        t.penup()
        t.setposition(-220,200)
        t.pendown()
        t.pen(pencolor={},pensize=1,speed=10).format("blue")# color given

        if order == 0:
            t.forward(size)
        else:
            for angle in [60, -120, 60, 0]:
               koch(order-1, size/3)
               t.left(angle)

if __name__ == '__main__':

    axiom = "F-F+F+FF-F-F+F"
    axiom = iterate(axiom, 3, "F-F-F-F")
    draw(axiom, 90, 2)
