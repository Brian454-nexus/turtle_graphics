from turtle import *
import colorsys

# Set up the turtle
speed(0)
bgcolor('black')
h = 0.8

# Function to draw a star
def draw_star(size, color):
    begin_fill()
    fillcolor(color)
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

# Main drawing loop
i = 0
while True:
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.004
    pensize(i % 5 + 1)  # Vary the pen size

    # Draw a star
    draw_star(i, c)

    # Move the turtle in a spiral pattern
    forward(i * 2)
    right(45)
    forward(i)
    right(90)

    i += 1

done()
