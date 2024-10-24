import turtle
import time
import random

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("navy")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("dark green")
food.penup()
food.goto(0, 100)

# Segments
segments = []

# Score
score = 0
high_score = 0
delay = 0.1

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to control the snake's direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

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

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 10
        if score > high_score:
            high_score = score

        # Update the score display
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        delay -= 0.001

    # Move the segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collisions with walls
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset score
        score = 0
        delay = 0.1

        # Update the score display
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with itself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset score
            score = 0
            delay = 0.1

            # Update the score display
            score_display.clear()
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
