import turtle
tt=turtle.Turtle()
turtle.bgcolor("cyan")
tt.pencolor("darkblue")
tt.speed(0)
tt.penup()
tt.goto(0,200)
tt.pendown()
forDis=0
dR=0
while(True):
    tt.forward(forDis)
    tt.right(dR)
    forDis+=1.75
    dR+=0.5
    if dR==1000:
        break
    tt.hideturtle()
turtle.done