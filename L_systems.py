import turtle

#I tried using create_new_turtle_enviroment to assign all the listed states such
#as the speed of the turtle and starting position of the turtle so that I don't
#have to repeat code but I don't think Turtle supports this and making a class
#wouldn't work as well. Insetead, I made t = turtle.Turtle() global.

#Notes: Type name and color in strings if python 2.7 or less. elif, type just name and string.
#Notes: Start up the interpreter with pythonw2.7 if you want to use python 2.7 (recommended)
t = turtle.Turtle()
TurtleLand = turtle.Screen()

def create_LSystem(Iterations, axiom):
    """
    Creates an L-System using the axioms provided and Iterates over this L-System
    "Iterations-times" (n-times).
    For a Koch Fractal:
    axiom = F
    rule = F > F-F++F-F
    For a Sierpinski Triangle:
    axiom = S+M+M
    rules = S > S+M-S-M+S , M > MM
    For a Fractal Plant:
    axiom = C
    rules = C > M-[[C]+C]+M[+MC]-C, M > MM
    For every code:
    fractal = create_LSystem(Iterations, "axiom")
    draw_LSystem(t, fractal, angle, distance)
    #angle must be 120 for Sierpinski Triangle
    """
    starting_string = axiom
    end_string = ""

    for i in range(Iterations):
        end_string = translate_string(starting_string)
        starting_string = end_string

    return end_string

def translate_string(old_string):
    """
    Applies apply_rules to every character in the old_string and returns the
    new_string.
    """
    new_string = ""

    for character in old_string:
        new_string = new_string + apply_rules(character)

    return new_string

def apply_rules(character):
    """Applies each rule of the given axiom to each character given in old_string."""
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
    """Makes Jonathan draw the L-System using turtle and the instructions given."""
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
    """Tried to assign each feature to my turtle. """

    turtle.setup(1395,1200)
    t.penup()
    t.setposition(-650,-300)
    t.pendown()
    t.speed("fastest")
    TurtleLand.onkey(TurtleLand.bye, 'q')
    TurtleLand.listen()

def main():
    """The interactive part of the program."""

    after_instructions = "Now click on the other window to view your Koch fractal being made!"

    print("Hello! Welcome to the world of fractals!")
    # name = '"{0}"'.format(input("What's your name? ")) #have to type in a string for some reason
    # color = '"{0}"'.format(input("Hello "+ name +" .What's your favorite color? "))
    name = input("What's your name?  ")
    color = input("Hello "+ name +". What's your favorite color? ")
    print("Sweet! The interesting thing about fractals is that they use recursion," + "\n" +
    "just as our hw5 did. Here's an example of a fractal called a koch fractal," + "\n" +
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
    sierpinski_iterations = input("Type in how many times you want to iterate over (between 4 and 6): ")
    sierpinski_length = input("Now type in the length you want each line to be (between 5 and 10): ")
    t.reset()
    create_new_turtle_enviroment()
    t.speed("fastest")
    t.pen(pencolor=color)
    t.penup()
    t.setposition(-550,350)
    t.pendown()
    print(after_instructions)
    sierpinski_instructions = create_LSystem(sierpinski_iterations, "S+M+M")
    draw_LSystem(t, sierpinski_instructions, 120, sierpinski_length)


    print("Great! Lastly we'll be doing a fractal plant where you can chose to" + "\n" +
    "iterate as many times as you want, specifying the angele and length of each" + "\n" +
    "line.")
    fractal_plant_iterations = input("Type in how many times you want to iterate this fractal plant over (between 2 and 6): ")
    fractal_plant_angle = input("Now type in an angle for your fractal plant (between 15 and 40): ")
    fractal_plant_length = input("Lastly, type in the length you want your plant to start off with : ")
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
    print("Good job " + name + ". Now you're ready to create your own fractals!" + "\n" +
    "To create your own fractal, you first should start off with a base case axiom." + "\n" +
    "For example, the Fractal Plant base case is 'C' which simply means to do nothing." + "\n" +
    "However, the Sierpinski Triangle base case is S+M+M where both 'S' and 'M'" + "\n" +
    "mean draw forward, '+' means turn right by some angle and '-' means turn left " + "\n" +
    "by the same angle. Next, you assign some rules to each of your characters. In" + "\n" +
    "the case of your Fractal Plant, every 'C' in your current iteration is translated" + "\n" +
    "into 'M-[[C]+C]+M[+MC]-C' and every 'M' into 'MM' For example, the first iteration of" + "\n" +
    "your Fractal Plant will simply be 'C' while your fourth would look like:" + "\n" +
    "MMMMMMMM-[[MMMM-[[MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]" + "\n" +
    "+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]+MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]" + "\n" +
    "-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]+MMMM[+MMMMMM-[[M-[[C]+C]+M" + "\n" +
    "[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]-M" + "\n" +
    "M-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]" + "\n" +
    "+C]+M[+MC]-C]+MMMM-[[MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]" + "\n" +
    "+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]+MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]" + "\n" +
    "+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]+MMMM[+MMMMMM-[[M-[[C]+C]+M[+MC]" + "\n" +
    "-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]-MM-[[M-[" + "\n" +
    "[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]" + "\n" +
    "-C]+MMMMMMMM[+MMMMMMMMMMMM-[[MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MM" + "\n" +
    "M-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]+MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]" + "\n" +
    "-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]+MMMM[+MMMMMM-[[M-[[C]+C]+M[+MC]" + "\n" +
    "-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]-MM-[[M-[[C]" + "\n" +
    "+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]-M" + "\n" +
    "MMM-[[MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[" + "\n" +
    "[C]+C]+M[+MC]-C]+MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[" + "\n" +
    "+MC]-C]-M-[[C]+C]+M[+MC]-C]+MMMM[+MMMMMM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+C]+M[+MC]-" + "\n" +
    "C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C]-MM-[[M-[[C]+C]+M[+MC]-C]+M-[[C]+" + "\n" +
    "C]+M[+MC]-C]+MM[+MMM-[[C]+C]+M[+MC]-C]-M-[[C]+C]+M[+MC]-C" + "\n" +
    "Pretty lengthy right? Thats why the fractal plant took longer to draw!" + "\n" +
    "Lastly, the '[' character simply saves your current position while ']' takes" + "\n" +
    "you back to that position. Now that you know how fractals work, you can create" + "\n" +
    "your own! Simply establish an axiom and rules using (in the case of our Fractal Plant):" + "\n" +
    "my_instructions = L_System(axiom = ['C'], rules = {'C': [ 'M', '-', '[', '[', 'C', ']'," + "\n" +
    "'+', 'C', ']', '+', 'M', '[', '+', 'M', 'C', ']', '-', 'C', ], 'M': ['M', 'M']})" + "\n" +
    "or set my_instructions = create_LSystem(Iterations, axiom) and type this in to run your own fractal code!:" + "\n" +
    "draw_LSystem(t, my_instructions, your assigned angle, your assigned length of line)." + "\n" +
    "Great job "+ name+"! Type in 'main()' to run this tutorial again or get creative and make your own fractals!")

class L_System():
    """
    A class that takes your starting axiom and dictionary of rules, and returns
    a string that works as instructions for draw_LSystem(t, instructions, andle, distance).
    L_System(axiom, rules)
    See examples of axioms and rules in the uppermost docstring.
    """
    def __init__(self, axiom, rules):
        """
        Initiates each L_system with its axiom and given rules in this format:
        axiom = [ 'S', '+', 'M', '+', 'M' ],
        rules = { 'S': [ 'S', '+', 'M', '-', 'S', '-', 'M', '+', 'S' ], 'M': [ 'M', 'M' ] }
        """
        self.axiom = axiom
        self.rules = rules

    def translate(self, iteration):
        """ Evaluates each character in your axiom."""

        for character in self.axiom:
            self.translate_character(character,iteration)

    def translate_character(self, character, iteration):
        """ Recursively translates each character using the given rules. """
        final_instructions = []

        for keys in self.rules:
            if iteration <= 0 or character not in self.rules:
                character = character
            else:
                for new_character in self.rules[character]:
                    self.translate_character(new_character, iteration-1)

    main()
