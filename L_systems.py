import turtle

# make this a class at some point
t = turtle.Turtle()
TurtleLand = turtle.Screen()

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

    For a Fractal Plant:
    rule = X > M-[[X]+X]+M[+MX]-X, M > MM
    axiom = X

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
    elif character == 'S':
        rule = 'S+M-S-M+S'
    elif character == 'M':
        rule = 'MM'
    elif character == 'C':
        rule = 'M-[[C]+C]+M[+MC]-C'
    else:
        rule = character

    return rule

def draw_LSystem(Jonathan, instructions, angle, distance):
    """
    Makes Jonathan draw the L-System using turtle and the instructions given.
    """
    stack  = []

    for command in instructions:
        if command == 'F' or command == 'M' or command == 'S' or command == 'P':
            Jonathan.forward(distance)
        elif command == 'B':
            Jonathan.backward(distance)
        elif command == 'C':
            Jonathan.left(360)
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

def create_new_turtle_enviroment():
    turtle.setup(1395,1200)
    t.penup()
    t.back(500)
    t.pendown()
    TurtleLand.onkey(TurtleLand.bye, 'q')
    TurtleLand.listen()

def main():
    """
    The main function being passed as an example.
    """
    after_instructions = "Now click on the other window to view your Koch fractal being made!"

    print("Hello! Welcome to the world of fractals!")
    # name = '"{0}"'.format(input("What's your name? ")) #have to type in a string for some reason
    # color = '"{0}"'.format(input("Hello "+ name +" .What's your favorite color? "))
    name = input("What's your name? ")
    color = input("Hello "+ name +". What's your favorite color? ")
    print("Sweet! The interesting thing about fractals is that they use recursion," + "\n" +
    "just as our hw5 did." "Here's an example of a fractal called a koch fractal," + "\n" +
    "named after the Swedish Mathematician Helge von Koch.")
    create_new_turtle_enviroment()
    TurtleLand.title("" + name + "'s Fractal!")
    t.pen(pencolor=color)
    t.speed("fastest")
    koch_instructions = create_LSystem(4, "F")
    print("Fractals can be iterated as many times as you choose, but for now we'll" + "\n" +
    "set it at 4 iterations.")
    koch_angle = input("Type in an angle between 50 and 100 for our koch fractal: ")
    koch_length = input("Now type in a length between 10 and 30 for your lines: ")
    print(after_instructions)
    draw_LSystem(t, koch_instructions, int(koch_angle), int(koch_length))   # draw the picture at (angle 60, length 5)
    print("What you saw was a Koch fractal iterated over four times, with an angle" + "\n" +
    "of {} and a length {}.").format(koch_angle,koch_length)


    print("Now lets try to do a Sierpinski Triangle fractal! In this case, you'll" + "\n" +
    "be choosing how many iterations you want instead of the angle.")
    sierpinski_iterations = input("Type in how many times you want to iterate over (between 2 and 6): ")
    sierpinski_length = input("Now type in the length you want each line to be (between 5 and 10): ")
    create_new_turtle_enviroment()
    t.reset()
    t.speed("fastest")
    t.pen(pencolor=color)
    t.penup()
    t.setposition(-500,0)
    t.pendown()
    print(after_instructions)
    sierpinski_instructions = create_LSystem(sierpinski_iterations, "S+M+M")
    draw_LSystem(t, sierpinski_instructions, 120, sierpinski_length)


    print("Great! Lastly we'll be doing a fractal plant where you can chose to" + "\n" +
    "iterate as many times as you want, specifying the angele and length of each" + "\n" +
    "line.")
    fractal_plant_iterations = input("Type in how many times you want to iterate this fractal plant over: ")
    fractal_plant_angle = input("Now type in an angle for your fractal plant: ")
    fractal_plant_length = input("Lastly, type in the length you want your plant to start off with: ")
    t.reset()
    t.pen(pencolor=color)
    t.penup()
    t.setposition(-500,0)
    t.left(40)
    t.pendown()
    t.speed("fastest")
    print(after_instructions)
    fractal_plant_instructions = create_LSystem(fractal_plant_iterations, 'C')
    draw_LSystem(t, fractal_plant_instructions, fractal_plant_angle, fractal_plant_length)
    print("Good job " + name + ". Now you're ready to create your own fractals!"
    "To create your own fractal, you first should start off with a base case axiom." + "\n" +
    "For example, the Sierpinski Triangle base case is S+M+M where both 'S' and 'M'" + "\n" +
    "mean draw forward, '+' means turn right by some angle and '-' means . Next," + "\n" +
    "apply some rules to" )
    #rule = S > S+M-S-M+S , M > MM
    #axiom = S+M+M


#print("These are the instructions being iterated over" + "\n" + inst)
if __name__ == "__main__":
    main()
