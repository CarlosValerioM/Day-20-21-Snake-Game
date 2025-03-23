#!/usr/bin/env python3
"""
snakeGame.py - A simple Snake game implemented with the turtle graphics library.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/23
License: MIT
Dependencies: turtle, random, time

Description:
This script implements a simple Snake game using the turtle graphics library.
The snake moves around the screen, and the player controls its direction using the arrow keys.
The snake grows in size each time it eats food, and the game checks for collisions
with itself or the food. The game ends when the snake collides with itself.

The script includes the following functions:
1. `move_up()`, `move_down()`, `move_left()`, `move_right()`: Control the snake's movement.
2. `check_collision_front()`: Checks for collisions between the snake's head and other objects.

Usage:
Run the script and control the snake with the arrow keys:
    python snakeGame.py

Example Output:
    The snake moves in the direction of the arrow key pressed.
    The snake grows each time it eats the food.
    The game ends if the snake collides with itself.
"""

import time  # Imports the time module to manage pauses in the game
import turtle as t  # Imports the Turtle module for graphics
import random  # Imports random to generate random positions
import game_intelligence as gi  # Imports a custom module for game logic

def main():
    # Game screen setup
    screen = t.Screen()
    screen.setup(width=800, height=500)  # Sets the window size
    screen.listen()  # Enables key event detection

    # Creating the snake as a list of segments
    snake = []
    for i in range(3):  # The snake starts with 3 segments
        head = t.Turtle()  # Creates a new segment
        head.shape("square")  # Represents it as a square
        head.penup()  # Disables line drawing when moving
        head.goto(i * 20, 0)  # Positions segments in a row
        snake.append(head)  # Adds the segment to the snake list

    # Creating the food
    food = t.Turtle()
    food.shape("circle")  # The food is a circle
    food.penup()
    food.goto(random.randint(-400, 400), random.randint(-250, 250))  # Random position

    game_active = True  # Controls whether the game is running

    # Assigning controls to move the snake
    screen.onkey(lambda: gi.move_up(snake[0], snake[0].xcor(), snake[0].ycor()), "Up")
    screen.onkey(lambda: gi.move_down(snake[0], snake[0].xcor(), snake[0].ycor()), "Down")
    screen.onkey(lambda: gi.move_left(snake[0], snake[0].xcor(), snake[0].ycor()), "Left")
    screen.onkey(lambda: gi.move_right(snake[0], snake[0].xcor(), snake[0].ycor()), "Right")

    # Main game loop
    while game_active:
        screen.update()  # Updates the screen
        time.sleep(0.1)  # Short pause to control game speed

        # Checks if the snake eats the food
        if gi.check_collision_front(snake[0], food):
            bodypart = t.Turtle()  # Creates a new snake segment
            bodypart.shape("square")
            bodypart.penup()
            snake.append(bodypart)  # Adds the new segment to the snake

            # Moves the food to a new random position
            food.goto(random.randint(-400, 400), random.randint(-250, 250))

        # Moves the snake's body
        for bodypart in range(len(snake) - 1, 0, -1):
            oldx, oldy = snake[bodypart - 1].xcor(), snake[bodypart - 1].ycor()
            snake[bodypart].goto(oldx, oldy)

        # Checks if the snake collides with itself
        for bodypart in snake:
            game_active = False if gi.check_collision_front(snake[0], bodypart) else True

        # Moves the snake's head forward
        snake[0].forward(20)

    screen.mainloop()  # Keeps the window open when the game ends

if __name__ == '__main__':
    main()
