import turtle
import random
import time

# Initial game variables
delay = 0.1
score = 0
highest_score = 0

# Snake body segments list
bodies = []

# Set up the screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)

# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.fillcolor("green")
food.penup()
food.goto(0, 200)

# Scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, 250)  # Move to the top of the screen for better visibility
sb.write("Score: 0 | Highest Score: 0", align="center", font=("Arial", 24, "normal"))

# Define movement functions
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling - key mappings
s.listen()
s.onkey(move_up, "Up")
s.onkey(move_down, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")
s.onkey(move_stop, "space")

# Main game loop
while True:
    s.update()

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide snake bodies
        for body in bodies:
            body.goto(1000, 1000)  # Move off-screen
        bodies.clear()

        # Reset score and delay
        score = 0
        delay = 0.1

        # Update the scoreboard
        sb.clear()
        sb.write(f"Score: {score} | Highest Score: {highest_score}", align="center", font=("Arial", 24, "normal"))

    # Check collision with food
    if head.distance(food) < 20:
        # Move the food to a new random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment to the snake
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        body.penup()
        bodies.append(body)

        # Increase the score
        score += 10

        # Shorten the delay to make the game faster
        delay -= 0.001

        # Update the highest score
        if score > highest_score:
            highest_score = score
        sb.clear()
        sb.write(f"Score: {score} | Highest Score: {highest_score}", align="center", font=("Arial", 24, "normal"))

    # Move the snake body segments
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with the snake's own body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the bodies
            for body in bodies:
                body.goto(1000, 1000)
            bodies.clear()

            # Reset score and delay
            score = 0
            delay = 0.1

            # Update the scoreboard
            sb.clear()
            sb.write(f"Score: {score} | Highest Score: {highest_score}", align="center", font=("Arial", 24, "normal"))

    time.sleep(delay)
