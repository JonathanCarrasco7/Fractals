import turtle

def create_LSystem(Iterations,axiom):
    """
    Creates an L-System using the axioms provided and Iterates over this L-System
    "Iterations-times" (n-times).
    For a Koch Fractal:
    rule = F > F-F++F-F
    axiom = F

    For a Sierpinski Triangle:
    rule = S > S+M-S-M+S , M > MM
    axiom = S+M+M

    For every code:
    fractal = create_LSystem(Iterations, "axiom")
    draw_LSystem(t, fractal, angle, distance)
    #angle must be 120 for Sierpinski Triangle
    """

    starting_string = axiom
    end_string = ""
    for i in range(Iterations):
        end_string = process_string(starting_string)
        starting_string = end_string

    return end_string

def process_string(old_string):
    """
    Applies apply_rules to every character in the old_string and returns the
    new_string.
    """

    new_string = ""
    for character in old_string:
        new_string = new_string + apply_rules(character)

    return new_string

def apply_rules(character):
    """
    Applies each rule of the given axiom to each character given in old_string.
    """

    rule = ""
    if character == 'F':
        rule = 'F-F++F-F'
    #elif character == 'S':
        #rule = 'S+M'
    else:
        rule = character

    return rule

def draw_LSystem(Jonathan, instructions, angle, distance):
    """
    Makes Jonathan draw the L-System using turtle and the instructions given.
    """
    stack  = []

    for command in instructions:
        if command == 'F' or command == 'M' or command == 'S':
            Jonathan.forward(distance)
        elif command == 'B':
            Jonathan.backward(distance)
        elif command == '+':
            Jonathan.right(angle)
        elif command == '-':
            Jonathan.left(angle)
        elif command == '[':
            stack.append((Jonathan.heading(), Jonathan.pos()))
        elif command == ']':
            heading, position = stack.pop()
            Jonathan.penup()
            Jonathan.goto(position)
            Jonathan.setheading(heading)
            Jonathan.pendown()

def main():
    """
    The main function being passed as an example.
    """

    print("Hello! Welcome to the world of fractals!"+ "\n")
    name = input("What's your name? ")
    color = input("Hello "+ name +".What's your favorite color?")
    print("Sweet! The interesting thing about fractals is that they use recursion,
    "just as our hw5 did. Here's an example of a fractal called a koch fractal,
    "named after some dude who's name ILL PUT IN LATER. But first, type 'main()'.")
    #print("These are the instructions being iterated over" + "\n" + inst)
    t = turtle.Turtle()
    TurtleLand = turtle.Screen()
    t.pen(pencolor=name)
    t.up()
    t.back(200)
    t.down()
    t.speed("fastest")
    my_angle = input("Give me an angle ")
    my_length = input("length ")
    draw_LSystem(t, inst, int(my_angle), int(my_length))   # draw the picture at (angle 60, length 5)
    TurtleLand.onkey(TurtleLand.bye, 'q')
    TurtleLand.listen()

if __name__ == "__main__":
    main()
