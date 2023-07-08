import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
correct_guess = None
correct_answers = None
t = turtle.Turtle()

guessed_states = []
number = 0
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{number}/50 States Correct", prompt="Enter the state:").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missed_data = pandas.DataFrame(missing_states)
        missed_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        t.hideturtle()
        t.penup()
        correct_guess = states_data[states_data.state == answer_state]
        t.goto(int(correct_guess.x.iloc[0]), int(correct_guess.y.iloc[0]))
        t.write(correct_guess.state.item(), align='center')

        if answer_state not in guessed_states:
            number += 1
            guessed_states.append(answer_state)












## Find Coordinates to display the name of each state
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

