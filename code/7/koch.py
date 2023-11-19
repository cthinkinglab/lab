import turtle

def koch(t, order, size):
    if order == 0:                  # The base case is just a straight line
        t.forward(size)
        
    else:
        koch(t, order-1, size/3)    # koch-ify the 1st line
        t.left(60)                  # rotate 60deg to the left
        koch(t, order-1, size/3)    # koch-ify the 2nd line
        t.right(120)                # rotate 120deg to the right
        koch(t, order-1, size/3)    # koch-ify the 3rd line
        t.left(60)                  # rotate 60deg to the left
        koch(t, order-1, size/3)

def main():
    pen = turtle.Turtle(shape="turtle")
    screen = turtle.Screen()
    screen.title('Turtle Koch Curve')

    pen.color("green")
    pen.shapesize(1)    
    pen.penup()
    pen.speed('fastest')
    pen.backward(150)
    pen.pendown()

    koch(pen, 3, 300)

    screen.exitonclick()

if __name__ == '__main__':
    main()
