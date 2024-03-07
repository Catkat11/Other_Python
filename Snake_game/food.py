from turtle import Turtle
import random

class Food(Turtle):
    """A class representing the food object in the snake game."""

    def __init__(self):
        """Initialize the food object."""
        super().__init__()  # Initialize the parent class (Turtle)
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to prevent drawing lines when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the speed of the food to the fastest
        self.refresh()  # Call the refresh method to position the food randomly

    def refresh(self):
        """Move the food to a random location on the screen."""
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen boundaries
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen boundaries
        self.goto(random_x, random_y)  # Move the food to the random coordinates
