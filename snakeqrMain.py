import turtle
import time
import random
wn=turtle.Screen()
wn.title("Sake in Code")
wn.setup(width=600,height=600)
wn.tracer(0)
head=turtle.Turtle();
head.speed(0);head.shape("square");
head.color("black");
head.penup();
head.goto(0,0)
head.direction="stop"
food=turtle.Turtle();
food.speed(0);
food.shape("circle");
food.color("red");
food.penup();
food.goto(50,50)
sgs=[]
def go_up():
    head.direction="up"
def go_down():
    head.direction="down"
def go_right():
    head.direction="right"
def go_left():
    head.direction="left"
def move():
    x=head.xcor();y=head.ycor()
    if head.direction=="up":
        head.sety(y+20)
    if head.direction=="down":
        head.sety(y-20)
    if head.direction=="left":
        head.setx(x-20)
    if head.direction=="right":
        head.setx(x+20)
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()
    if head.xcor()>290 or head.xcor()< -290 or head.ycor()>290 or head.ycor()< -290:
        time.sleep(1)
        break
    if head.distance(food)<20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        sg=turtle.Turtle()
        sg.speed(0)
        sg.shape("square")
        sg.color("grey")
        sg.penup()
        sgs.append(sg)
    for index in range(len(sgs)-1,0,-1):
        x=sgs[index-1].xcor()
        y=sgs[index-1].ycor()
        sgs[index].goto(x,y)
    if len(sgs)>0:
        x=head.xcor()
        y=head.ycor()
        sgs[0].goto(x,y)
    move()
    
    time.sleep(0.1)
