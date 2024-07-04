import turtle

t = turtle

turtle.pensize(4)
colors = []
for i in range(0, 16777215):
    colors.append("#"+hex(i))
numberrounds = int(input("Enter the number of rounds: "))

for i in range(50):
    t.pencolor(colors[i%numberrounds])
    t.circle(i*4, 100)

t.exitonclick()