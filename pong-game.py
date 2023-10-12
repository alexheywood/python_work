import turtle
import os

#setup canvas
wn = turtle.Screen()
wn.title("Pong by @alexheywood")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#left paddle

paddlea = turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.shapesize(stretch_wid=5, stretch_len=1)
paddlea.color("white")
paddlea.penup()
paddlea.goto(-350, 0)


#right paddle

paddleb = turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.shapesize(stretch_wid=5, stretch_len=1)
paddleb.color("white")
paddleb.penup()
paddleb.goto(350, 0)


#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07

#scorecards
player_a_score = 0
player_b_score = 0

score_a_string = "Player A: "
score_b_string = "  Player B: "
score_string = score_a_string + str(player_a_score) + score_b_string + str(player_b_score)

#Score Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(score_string, align="center", font=("Courier", 18, "normal"))

#scorecards
player_a_score = 0
player_b_score = 0


def player_a_scored():
    global player_a_score
    global score_string
    player_a_score += 1
    print(player_a_score)
    update_scoreboard()
    
def player_b_scored():
    global player_b_score
    player_b_score += 1
    print(player_b_score)
    update_scoreboard()
    os.system("aplay bounce.wav&")

def update_scoreboard():
    pen.clear()
    score_string = score_a_string + str(player_a_score) + score_b_string + str(player_b_score)
    pen.write(score_string, align="center", font=("Courier", 18, "normal"))

#keyboard functions

def left_paddle_up():
    y = paddlea.ycor()
    y += 20
    paddlea.sety(y)


def left_paddle_down():
    y = paddlea.ycor()
    y -= 20
    paddlea.sety(y)

def right_paddle_up():
    y = paddleb.ycor()
    y += 20
    paddleb.sety(y)


def right_paddle_down():
    y = paddleb.ycor()
    y -= 20
    paddleb.sety(y)

#keyboard bindings
    
wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")


#Main game loop

while True:
    wn.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border collision

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_scored()

        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        player_b_scored()

    #paddle collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleb.ycor() + 40 and ball.ycor() > paddleb.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddlea.ycor() + 40 and ball.ycor() > paddlea.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

