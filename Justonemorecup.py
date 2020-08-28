import turtle
import random

#Screen
wn = turtle.Screen()
wn.bgcolor("brown")
wn.setup(width=1000, height=800)
wn.title("Just one more cup")
wn.addshape("cup.gif")
wn.addshape("coffe drop.gif")
wn.addshape("mouth.gif")
wn.tracer(0)

score = 0
lives = 3
d = 0


#Player
player = turtle.Turtle()
player.speed(0)
player.shape("cup.gif")
player.color("orange")
player.setheading(90)
player.penup()
player.goto(0,-300)
player.direction = "stop"

#Coffe
coffes = []
for _ in range(10):
    coffe = turtle.Turtle()
    coffe.speed(0)
    coffe.shape("coffe drop.gif")
    coffe.color("orange")
    coffe.setheading(90)
    coffe.penup()
    coffe.x = 0
    coffe.goto(200,340)
    coffes.append(coffe)

#Mouth
mouths = []
for _ in range(3):
    mouth = turtle.Turtle()
    mouth.speed(0)
    mouth.shape("mouth.gif")
    mouth.color("orange")
    mouth.setheading(90)
    mouth.penup()
    mouth.x = 0
    mouth.goto(-200,340)
    mouths.append(mouth)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("orange")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
font = ("Calibri", 24, "normal")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

#MOVEMENT
def move_left():
    player.direction = "left"

def move_right():
    player.direction = "right"


turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(move_left, "A")
turtle.onkey(move_right, "D")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

    
#Main game loop
while True:
        wn.update()
        #Move the player
        if player.direction == "left":
                x = player.xcor()
                x -= 0.5
                player.setx(x)

        if player.direction == "right":
                x = player.xcor()
                x += 0.5
                player.setx(x)

        #Move the coffe
        for coffe in coffes:
            y = coffe.ycor()
            y -= random.randint(1, 3)
            coffe.sety(y)

            if y < -320:
                x = random.randint(-500, 500)
                y = random.randint(300, 400)
                coffe.goto(x,y)

            #Check for collision with the player
            if player.distance(coffe) < 40:
                x = random.randint(-500, 500)
                y = 320
                coffe.goto(x,y)
                score += 10
                pen.clear()
                pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

                
        #Move the coffe
        for mouth in mouths:
            y = mouth.ycor()
            y -= random.randint(1, 3)
            mouth.sety(y)

            if y < -320:
                x = random.randint(-500, 500)
                y = random.randint(300, 400)
                mouth.goto(x,y)

            #Check for collision with the player
            if player.distance(mouth) < 40:
                x = random.randint(-500, 500)
                y = 320
                coffe.goto(x,y)
                player.goto(0,-300)
                player.direction = "stop"
                mouth.goto(random.randint(-500, 500), random.randint(300, 400))
                lives -= 1
                pen.clear()
                pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

        if lives < 1:
            lives = 3
            player.goto(0, -300)
            score = 0
            pen.clear()
            pen.goto(0,260)
            font = ("Calibri", 24, "normal")
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
                                                        
wn.mainloop()

