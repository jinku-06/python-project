import turtle
import pandas

screen = turtle.Screen()
screen.title("Map")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# Data variable to read the csv file
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 States Correct', prompt="What's the next state? ").title()

    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        position = data[data.state == answer_state]
        t.goto(int(position.x), int(position.y))
        t.write(position.state.item())

# USING LIST COMPREHENSION TO STORE THE STATE THAT USER COULD NOT ANSWER
missing_state = [state for state in all_states if state not in guessed_state]
new_data = pandas.DataFrame(missing_state)
new_data.to_csv('sates_to_learn.csv')




