import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    t = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    t.shape('turtle')
    # Set your turtle's speed using .speed(2)
    t.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    t.color('green')
    t.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range(4):
        t.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        t.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    #yes
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    t.penup()
    t.goto(50, 50)
    t.pendown()
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    t.circle(50, steps=30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    t.begin_fill()
    # Draw 3 more shapes with different fill colors!
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    for i in range(3):
        t.forward(75)
        t.right(120)
        t.end_fill()
    t.penup()
    t.goto(-120, 100)
    t.pendown()
    for i in range(5):
        t.forward(75)
        t.left(72)
    for i in range(6):
        t.forward(100)
        t.left(60)
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
