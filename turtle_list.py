import turtle

turtle.bgcolor("crimson")
turtle.shape('turtle')


my_colors = ['purple', 'yellow', 'red', 'green']


def draw_circle():
    for literally_anything in range(4):
        print("my postion in the list is is currently = ", literally_anything)
        turtle.forward(60)
        turtle.right(90)
    
def draw_colored_circle(colors):
    for color in colors:
            turtle.color(color)
            draw_circle()
            turtle.left(30)

draw_colored_circle(my_colors)
turtle.done()