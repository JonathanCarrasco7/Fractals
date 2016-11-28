import turtle

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
        result = ''
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
    for i in xrange(0, num):
        # Translates the rule string for each iteration
        result = translate(result, axiom)
    return result

def draw(axiom, d=D, l=L):
    """
    Uses turtle to draw the L-System
    """
    stack  = []                 # Tracks the turtle's position
    screen = turtle.Screen()
    alex   = turtle.Turtle()

    alex.hideturtle()           # Doesn't show the turtle
    alex.speed(0)               # Makes the turtle faster
    alex.left(90)               # Points upwards instead of rightwards

    for i in xrange(len(axiom)):
        c = axiom[i]

        if c == 'F':
            alex.forward(l)

        if c == 'f':
            alex.penup()
            alex.forward(l)
            alex.pendown()

        if c == '+':
            alex.left(d)

        if c == '-':
            alex.right(d)

        if c == '[':
            stack.append((alex.heading(), alex.pos()))

        if c == ']':
            heading, position = stack.pop()
            alex.penup()
            alex.goto(position)
            alex.setheading(heading)
            alex.pendown()

    screen.onkey(screen.bye, 'q')
    screen.listen()
    turtle.mainloop()

if __name__ == '__main__':

    axiom = "F-F+F+FF-F-F+F"
    axiom = iterate(axiom, 3, "F-F-F-F")
    draw(axiom, 90, 2)

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
    def Fibonacci(t):
        pass

    def Mandlebrot(t):
        pass

    def Tree(t, order, size):
        pass
