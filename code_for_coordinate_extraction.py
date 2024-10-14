import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("Extract State Coordinates")
image = 'blank_states.png'  # Use your image file here
screen.setup(width=550, height=550)
screen.bgpic(image)  # Set the background image

# Initialize a list to store state names and their coordinates
coordinates = []

def get_coordinates(x, y):
    # Get the state name from user input
    state_name = turtle.textinput("State Name", "Enter the name of the state:")
    if state_name:
        # Store the coordinates and state name
        coordinates.append((state_name, x, y))
        print(f"State: {state_name}, X: {x}, Y: {y}")  # Print to console for reference

# Set up mouse click event
turtle.onscreenclick(get_coordinates)

# Instruction
turtle.write("Click on the states to get their coordinates.", align="center", font=("Arial", 12, "normal"))

# Keep the window open until closed by the user
turtle.mainloop()

# After collecting all coordinates, save to CSV
df = pd.DataFrame(coordinates, columns=["Name", "X-co", "Y-co"])
df.to_csv("states_coordinate.csv", index=False)
