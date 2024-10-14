import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("Indian-states-GUESS-GAME")
image = 'blank_states.png'
screen.setup(width=550, height=550)
turtle.bgpic(image)  # Set the background image
df = pd.read_csv('states_coordinate.csv')
num_state = len(df.Name.to_list())
while num_state > 0:
    text_in = turtle.textinput(f'Entry Box', 'Enter the State Name?').upper()
    if text_in in df['Name'].to_list():
        row_data = df[df['Name'] == text_in]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(row_data.x.item(), row_data.y.item())
        new_turtle.write(text_in.upper())
    if text_in == 'EXIT':
        turtle.clearscreen()
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()  # Set a solid color background
        new_turtle.goto(0, 0)  # Move turtle to the center
        font_style = ("Arial", 16, "bold")  # Font type, size, and style
        new_turtle.write('GAME OVER!', align="center", font=font_style)
        break
    num_state -= 1
screen.mainloop()
