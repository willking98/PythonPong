import turtle 

image = "/Users/Will/Desktop/Misc/grad_pic_head.gif"
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)
wn.bgcolor("black")
wn.addshape(image)
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape(image)
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 290)
pen.clear()
pen.write("Player 1 score: " + str(score_a) +  "                   Player 2 score: " + str(score_b), align="center", font=("Courier", 18, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "q")
wn.onkeypress(paddle_a_down, "a")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")    


# Main game loop
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1

    elif ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1

    # Sides
    if ball.xcor() > 400:
        ball.sety(0)
        ball.setx(0)
        score_a += 1
        pen.clear()
        pen.write("Player 1 score: " + str(score_a) +  "                   Player 2 score: " + str(score_b), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -400:
        ball.sety(0)
        ball.setx(0)
        score_b += 1
        pen.clear()
        pen.write("Player 1 score: " + str(score_a) +  "                   Player 2 score: " + str(score_b), align="center", font=("Courier", 18, "normal"))



    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
