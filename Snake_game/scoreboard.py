from turtle import Turtle

ALIGNMENT = "center"  # Text alignment for the scoreboard
FONT = "Arial", 24, "normal"  # Font style for the scoreboard


class Scoreboard(Turtle):
    """A class representing the scoreboard in the snake game."""

    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()  # Initialize the parent class (Turtle)
        self.score = 0  # Initialize the score to zero
        with open("data.txt") as file:
            self.high_score = int(file.read())  # Read the high score from a file
        self.penup()  # Lift the pen to prevent drawing lines when moving
        self.color("white")  # Set the color of the scoreboard text to white
        self.goto(0, 265)  # Position the scoreboard at the top center of the screen
        self.update_scoreboard()  # Update the scoreboard text
        self.hideturtle()  # Hide the turtle icon

    def update_scoreboard(self):
        """Update the scoreboard text."""
        self.clear()  # Clear the previous scoreboard text
        self.write(f"Score is :{self.score} High score {self.high_score}", align=ALIGNMENT,
                   font=FONT)  # Write the updated scoreboard text

    def reset(self):
        """Reset the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score  # Update the high score if the current score is higher
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))  # Write the new high score to the file
        self.score = 0  # Reset the score to zero
        self.update_scoreboard()  # Update the scoreboard text

    def increase_score(self):
        """Increase the score by 1."""
        self.score += 1  # Increment the score by 1
        self.update_scoreboard()  # Update the scoreboard text
