import turtle

def create_LSystem(Iterations,axiom):
    """
    Creates an L-System using the axioms provided and Iterates over this L-System
    "Iterations-times" (n-times).
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
        new_stringstr = new_stringstr + apply_rules(character)

    return new_string

def apply_rules(character):
    """
    Applies each rule of the given axiom to each character given in old_string.
    """

    new_string = ""
    if character == 'F':
        new_string = 'F-F++F-F'   # Rule 1
    else:
        new_stringstr = character   # no rules apply

    return new_string

def draw_LSystem(Jonathan, instructions, angle, distance):
    """
    Makes Jonathan draw the L-System using turtle and the instructions given.
    """

    for command in instructions:
        if command == 'F':
            Jonathan.forward(distance)
        elif command == 'B':
            Jonathan.backward(distance)
        elif command == '+':
            Jonathan.right(angle)
        elif command == '-':
            Jonathan.left(angle)

def main():
    """
    The main function being passed as an example.
    """

    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
