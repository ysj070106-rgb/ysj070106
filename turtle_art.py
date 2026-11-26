import turtle
import math

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("똥 그리기")
screen.tracer(1)

t = turtle.Turtle()
t.speed(8)
t.shape("turtle")
t.pensize(3)

FONT = "Malgun Gothic"


def ellipse(cx, cy, rx, ry, fill, outline="black"):
    t.penup()
    t.goto(cx + rx, cy)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    for angle in range(0, 361, 5):
        rad = math.radians(angle)
        t.goto(cx + rx * math.cos(rad), cy + ry * math.sin(rad))
    t.end_fill()


def triangle(p1, p2, p3, fill):
    t.penup()
    t.goto(p1)
    t.pendown()
    t.color("black", fill)
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)
    t.end_fill()


def bubble(x, y, text, size, tail_to):
    rx = size * (len(text) * 0.75 + 0.6)
    ry = size * 1.1
    triangle((x - size * 0.3, y), (x + size * 0.3, y), tail_to, "white")
    ellipse(x, y, rx, ry, "white")
    t.penup()
    t.goto(x, y - size * 0.75)
    t.color("black")
    t.write(text, align="center", font=(FONT, size, "bold"))


bubble(-200, 200, "응가", 22, (-120, 120))
bubble(-55, 225, "똥", 14, (-30, 150))
bubble(130, 200, "똥", 30, (80, 120))
bubble(230, 70, "똥", 14, (180, 20))
bubble(-200, -180, "소똥", 22, (-120, -110))
bubble(-20, -220, "새똥", 15, (0, -140))
bubble(170, -180, "말똥", 22, (100, -110))

BROWN = "#C8935A"
ellipse(0, -60, 165, 55, BROWN)
ellipse(0, 0, 120, 48, BROWN)
ellipse(5, 50, 75, 35, BROWN)
ellipse(15, 85, 28, 20, BROWN)

ellipse(-35, 0, 10, 13, "black")
ellipse(35, 0, 10, 13, "black")
ellipse(-32, 5, 3, 4, "white", "white")
ellipse(38, 5, 3, 4, "white", "white")

ellipse(-65, -25, 14, 8, "#F4A3A3", "#F4A3A3")
ellipse(65, -25, 14, 8, "#F4A3A3", "#F4A3A3")

t.pensize(2)
triangle((-12, -20), (12, -20), (0, -38), "#8B2E2E")

t.hideturtle()
screen.update()
turtle.done()