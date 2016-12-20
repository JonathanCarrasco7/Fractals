ls# Final Project Proposal
*High level summary of your project, including the things that* **you** *find interesting*
The purpose of this project will be to explore the recursive properties of
   fractals. I will be using L-systems and turtles, primarily to draw most of my fractals and attempt to use the Numba library in order to maximize time efficiency.

The L-systems will ideally be paired with instructions on the turtle library so
  that each recursive function is given drawing instructions. Additionally, the recursive functions will be customizable so that each instruction yields a different pattern and an additional argument will be the number of iterations the function goes through.

What I find interesting is the math behind fractals and how if you zoom in to a
 particular section of a fractal, it seems like its the original fractal. I also find the recursive nature of fractals and how they can be determined in terms of itself.


## Data Plan
*Summarize data sources, data formats, and how to obtain or generate the data you will be using*
The only data I would be involved with is simply reading about different kinds of
 fractals and more on L-systems but I wouldn't be opening data with CSV.

## Implementation Plan
*Overview of your plan. Are you starting from existing code? What skills from the course will be be using to complete your project? etc.*
I will be using prior knowledge of fractals and more recently acquired knowledge
  of recursive functions. Additionally, I will possibly be using the same code I've written before on the Cantor set and Mandlebrot set and modify it so that it will take different arguments of size and iterations.

### External Libraries
- Turtle

### Milestones
- L-systems paired with Turtle
- Recursion
- Interaction

## Deliverables
- An interactive interface
- A class that allows you to define your axiom and rules or
- Two functions that let you create your own L-System fractal
- Axioms and Rules for other fractals


# Final Project Report
*What you have achieved/learned*
I learned more about inheritance and a built-in python function named "input()".
I discovered L-Systems thanks to Julia and I know how to use turtle.Turtle().
Additionally, I used a little bit of recursion for translating rules and creating
L-systems and now have a good understanding on how to use axioms and rules for
creating fractals.

*What open questions remain*
I know want to learn more about turtle.RawTurtle(), how else to draw fractals (for
example, using pygame). and how, if possible, can I use my code to draw Mandlebrot
Set fractals. Also, I'd like to know what other libraries I would need to draw a
Mandlebrot Set fractal and I'm curious as to what differentiates L-System fractals
from other fractals.

## Instructions to run the code
$ from L_systems import *
The rest of the code is explained as you run the program!

#Notes:
Start up the interpreter with pythonw2.7 if you want to use python 2.7 (recommended)
Type in 'main()' to run the tutorial again
To create new instructions, type in create_LSystem() with number of iterations as
your first argument and starting axiom as second argument.
Then, draw your new fractal using draw_LSystem(t, new instructions, angle, distance).
To reset the canvas, type in turtle.reset()

---

# Final Project Grading

## Functionality 10/10

Impressive:  I loved that you wrote an L-system interpreter and connected it to the Turtle package.

## Challenge and Endurance 9/10

This was a challenging project and I know that you ran up against some obstacles but overcame them with
the L-Systems.

## Code Quality 6/10

Here's where I thought you struggled the most.  The code was not well-organized and lacked lots of basic
structure.  In particular, the long interactive threads with string after embedded string was not handled well.
It would have been better to put this in a separate file and imported it.  Or a text file and read it in.

## Final Product 9/10

Beautiful fractals, drawn before our eyes!  Lovely!

Overall: 44/50