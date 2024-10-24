import turtle  # Import the turtle graphics library for creating the game
import time  # Import the time library to create delays in the game
import random  # Import the random library to generate random positions for the food

# Set up the main window for the game
wn = turtle.Screen()  # Create a screen object to represent the game window
wn.title("Snake Game by Spandan Ghodke")  # Set the title of the window
wn.bgcolor("light green")  # Set the background color of the window
wn.setup(width=600, height=600)  # Define the dimensions of the window
wn.tracer(0)  # Disable automatic screen updates for smoother animation

# Create the snake's head
head = turtle.Turtle()  # Create a turtle object to represent the snake's head
head.shape("square")  # Set the shape of the head to a square
head.color("navy")  # Set the color of the head to navy
head.penup()  # Prevent the turtle from drawing lines as it moves
head.goto(0, 0)  # Move the head to the starting position at the center of the window
head.direction = "stop"  # Set the initial direction of the snake's movement

# Create the food for the snake
food = turtle.Turtle()  # Create a turtle object to represent the food
food.shape("circle")  # Set the shape of the food to a circle
food.color("dark green")  # Set the color of the food to dark green
food.penup()  # Prevent the food turtle from drawing lines as it moves
food.goto(0, 100)  # Position the food at a starting location

# Initialize the segments of the snake's body
segments = []  # Create an empty list to hold the segments of the snake

# Initialize score variables
score = 0  # Initialize the score to 0
high_score = 0  # Initialize the high score to 0
delay = 0.1  # Set the initial delay between movements

# Create a turtle to display the score
score_display = turtle.Turtle()  # Create a turtle object for displaying the score
score_display.speed(0)  # Set the speed of the score display turtle to maximum
score_display.color("black")  # Set the color of the score display to black
score_display.penup()  # Prevent the score display turtle from drawing lines
score_display.hideturtle()  # Hide the turtle cursor for the score display
score_display.goto(0, 260)  # Position the score display above the game area
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))  # Display the initial score

# Functions to control the snake's direction
def go_up():
    if head.direction != "down":  # Prevent the snake from going in the opposite direction
        head.direction = "up"  # Set the direction to up

def go_down():
    if head.direction != "up":  # Prevent the snake from going in the opposite direction
        head.direction = "down"  # Set the direction to down

def go_left():
    if head.direction != "right":  # Prevent the snake from going in the opposite direction
        head.direction = "left"  # Set the direction to left

def go_right():
    if head.direction != "left":  # Prevent the snake from going in the opposite direction
        head.direction = "right"  # Set the direction to right

# Function to move the snake in the current direction
def move():
    if head.direction == "up":  # If the snake is moving up
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y + 20)  # Move the head up by 20 units
    if head.direction == "down":  # If the snake is moving down
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y - 20)  # Move the head down by 20 units
    if head.direction == "left":  # If the snake is moving left
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x - 20)  # Move the head left by 20 units
    if head.direction == "right":  # If the snake is moving right
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x + 20)  # Move the head right by 20 units

# Keyboard bindings for controlling the snake
wn.listen()  # Start listening for keyboard events
wn.onkey(go_up, "w")  # Bind the 'w' key to the go_up function
wn.onkey(go_down, "s")  # Bind the 's' key to the go_down function
wn.onkey(go_left, "a")  # Bind the 'a' key to the go_left function
wn.onkey(go_right, "d")  # Bind the 'd' key to the go_right function

# Main game loop
while True:  # Start an infinite loop for the game
    wn.update()  # Refresh the screen

    # Check for collision with food
    if head.distance(food) < 20:  # If the snake's head is close enough to the food
        # Move the food to a random position
        x = random.randint(-290, 290)  # Generate a random x-coordinate
        y = random.randint(-290, 290)  # Generate a random y-coordinate
        food.goto(x, y)  # Move the food to the new random position

        # Add a new segment to the snake's body
        new_segment = turtle.Turtle()  # Create a new turtle for the segment
        new_segment.speed(0)  # Set the speed of the new segment to maximum
        new_segment.shape("square")  # Set the shape of the segment to square
        new_segment.color("gray")  # Set the color of the segment to gray
        new_segment.penup()  # Prevent drawing lines as it moves
        segments.append(new_segment)  # Add the new segment to the list of segments

        # Update score
        score += 10  # Increase the score by 10 points
        if score > high_score:  # If the current score exceeds the high score
            high_score = score  # Update the high score

        # Update the score display
        score_display.clear()  # Clear the previous score display
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))  # Display the updated score

        delay -= 0.001  # Decrease the delay to increase the speed of the game

    # Move the segments of the snake
    for index in range(len(segments) - 1, 0, -1):  # Loop through the segments in reverse order
        x = segments[index - 1].xcor()  # Get the x-coordinate of the segment in front
        y = segments[index - 1].ycor()  # Get the y-coordinate of the segment in front
        segments[index].goto(x, y)  # Move the current segment to the position of the segment in front

    if len(segments) > 0:  # If there are segments in the snake's body
        x = head.xcor()  # Get the current x-coordinate of the head
        y = head.ycor()  # Get the current y-coordinate of the head
        segments[0].goto(x, y)  # Move the first segment to the head's position

    move()  # Call the move function to update the head's position

    # Check for collisions with walls
    if (head.xcor() > 290 or head.xcor() < -290 or  # Check if the head is beyond the right or left wall
        head.ycor() > 290 or head.ycor() < -290):  # Check if the head is beyond the top or bottom wall
        time.sleep(1)  # Pause the game for a moment
        head.goto(0, 0)  # Reset the head position to the center of the window
        head.direction = "stop"  # Stop the head's movement

        for segment in segments:  # Loop through all segments
            segment.goto(1000, 1000)  # Move each segment off-screen
        segments.clear()  # Clear the list of segments

        # Reset score
        score = 0  # Reset the score to 0
        delay = 0.1  # Reset the delay to the initial value

        # Update the score display
        score_display.clear()  # Clear the previous score display
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))  # Display the reset score

    # Check for collision with itself
    for segment in segments:  # Loop through all segments
        if segment.distance(head) < 20:  # If the head is close to any segment
            time.sleep(1)  # Pause the game for a moment
            head.goto(0, 0)  # Reset the head position to the center of the window
            head.direction = "stop"  # Stop the head's movement

            for segment in segments:  # Loop through all segments
                segment.goto(1000, 1000)  # Move each segment off-screen
            segments.clear()  # Clear the list of segments

            # Reset score
            score = 0  # Reset the score to 0
            delay = 0.1  # Reset the delay to the initial value

            # Update the score display
            score_display.clear()  # Clear the previous score display
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))  # Display the reset score

    time.sleep(delay)  # Pause the loop for the current delay

wn.mainloop()  # Start the main event loop to keep the window open
