import turtle

t = turtle.Turtle()

t.pensize(4)
t.pencolor("green")

def shape(n,a):
    k = 180-(((n-2)*180)/n)
    for i in range(n):
        t.forward(a)
        t.left(k)
b = int(input("Enter the number of sides: "))

for _ in range(b):
    for i in range(10, 220, 10):
       shape(b,i)
    k = ((b-2)*180)/b
    t.left(k)

turtle.exitonclick()