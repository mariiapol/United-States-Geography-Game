import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()


data = pandas.read_csv("50_states.csv")
score = 0
list_state = data.state.to_list()
list_x = data.x.to_list()
list_y = data.y.to_list()
n = len(list_state)
name = "Guess the state"
list_g = []

while score <= 50:
    answer_state = str(screen.textinput(title=name, prompt="What's another state's name?"))

    if answer_state.title() == "Exit":
        states_to_learn = [state for state in list_state if state not in list_g]
        df = pandas.DataFrame(states_to_learn, columns=["State"])
        df.to_csv('states_to_learn.csv')

        break

    for i in range(n):
        if list_state[i] == answer_state.title():
            score += 1
            name = f"{score}/50 States Correct"
            tim.goto(int(list_x[i]), int(list_y[i]))
            tim.write(list_state[i])
            list_g.append(list_state[i])
#screen.exitonclick()
